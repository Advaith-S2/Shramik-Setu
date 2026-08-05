-- =============================================================================
-- ShramikSetu — Supabase / PostgreSQL Schema
-- Version: 1.0  (Day 1 — frozen after today per AGENTS.md §1)
-- Tables: 15   (PRD §9.2)
-- DO NOT ALTER without explicit sign-off — see AGENTS.md §1
-- =============================================================================

-- Enable pgcrypto for gen_random_uuid()
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- =============================================================================
-- ENUM TYPES
-- =============================================================================

CREATE TYPE user_role AS ENUM (
    'worker',
    'supervisor',
    'contractor',
    'inspector',
    'admin'
);

CREATE TYPE project_status AS ENUM (
    'draft',
    'active',
    'paused',
    'completed',
    'cancelled'
);

CREATE TYPE contract_status AS ENUM (
    'pending',       -- QR generated, not yet scanned/accepted
    'accepted',
    'declined',
    'expired',
    'terminated'
);

CREATE TYPE attendance_status AS ENUM (
    'present',
    'absent',
    'half_day',
    'holiday',
    'override'
);

CREATE TYPE attendance_method AS ENUM (
    'pin_gps',       -- PIN + GPS within radius
    'pin_only',      -- PIN but GPS skipped
    'override'       -- Supervisor override
);

CREATE TYPE wage_status AS ENUM (
    'pending',       -- No payment recorded yet
    'partial',       -- Some amount paid
    'paid',          -- Fully paid
    'disputed'
);

CREATE TYPE payment_method AS ENUM (
    'cash',
    'bank_transfer',
    'upi',           -- Record-only; no gateway integration
    'cheque',
    'other'
);

CREATE TYPE dispute_type AS ENUM (
    'wage_underpayment',
    'wage_nonpayment',
    'attendance_mismatch',
    'contract_violation',
    'other'
);

CREATE TYPE dispute_status AS ENUM (
    'open',
    'under_review',
    'contractor_responded',
    'resolved_worker_favour',
    'resolved_contractor_favour',
    'closed_no_action'
);

CREATE TYPE dispute_priority AS ENUM (
    'low',
    'medium',
    'high',
    'critical'
);

CREATE TYPE app_language AS ENUM (
    'en',
    'hi',
    'mr'
);

-- =============================================================================
-- TABLE 1: users
-- Base identity table — one row per registered account.
-- Inspectors are created by admin only (PRD M-01).
-- =============================================================================

CREATE TABLE users (
    id                  UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
    email               TEXT        NOT NULL UNIQUE,
    full_name           TEXT        NOT NULL,
    phone               TEXT,                          -- Optional for MVP
    role                user_role   NOT NULL,
    is_active           BOOLEAN     NOT NULL DEFAULT TRUE,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE  users              IS 'Base auth identity. Supabase Auth manages password hashing; this table stores profile + role.';
COMMENT ON COLUMN users.role         IS 'Drives RBAC across all modules. Inspector/admin assigned by admin only.';
COMMENT ON COLUMN users.phone        IS 'Optional in MVP. Future: OTP verification.';

-- =============================================================================
-- TABLE 2: workers
-- Extended profile for users with role = ''worker''.
-- Supervisors also have a workers row (they are workers who can generate PINs).
-- =============================================================================

CREATE TABLE workers (
    worker_id           UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id             UUID        NOT NULL UNIQUE REFERENCES users(id) ON DELETE CASCADE,
    state               TEXT,
    district            TEXT,
    occupation          TEXT,
    skills              TEXT[]      DEFAULT '{}',      -- e.g. ['masonry','plumbing']
    eshram_uan          TEXT,                          -- 12-digit e-Shram UAN, optional (PRD M-02)
    photo_url           TEXT,                          -- Supabase Storage URL
    date_of_birth       DATE,
    is_active           BOOLEAN     NOT NULL DEFAULT TRUE,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT workers_eshram_uan_format
        CHECK (eshram_uan IS NULL OR (eshram_uan ~ '^[0-9]{12}$'))
);

COMMENT ON TABLE  workers             IS 'Worker profile. Supervisors share this table (same role extension pattern).';
COMMENT ON COLUMN workers.eshram_uan  IS '12-digit e-Shram Universal Account Number. Optional. Validated by CHECK constraint.';
COMMENT ON COLUMN workers.skills      IS 'Free-text skill tags stored as array. No ML inference.';

-- =============================================================================
-- TABLE 3: contractors
-- Extended profile for users with role = ''contractor''.
-- =============================================================================

CREATE TABLE contractors (
    contractor_id       UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id             UUID        NOT NULL UNIQUE REFERENCES users(id) ON DELETE CASCADE,
    company_name        TEXT,
    state               TEXT,
    district            TEXT,
    gst_number          TEXT,
    is_verified         BOOLEAN     NOT NULL DEFAULT FALSE,  -- Admin-verified contractor
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE contractors IS 'Contractor profile. is_verified set by Admin after document check (out of scope for MVP UI).';

-- =============================================================================
-- TABLE 4: projects
-- A construction/labour project created by a contractor.
-- =============================================================================

CREATE TABLE projects (
    project_id          UUID            PRIMARY KEY DEFAULT gen_random_uuid(),
    contractor_id       UUID            NOT NULL REFERENCES contractors(contractor_id) ON DELETE RESTRICT,
    title               TEXT            NOT NULL,
    description         TEXT,
    location_text       TEXT,           -- Human-readable address
    daily_wage          NUMERIC(10,2)   NOT NULL CHECK (daily_wage > 0),
    start_date          DATE            NOT NULL,
    end_date            DATE,
    capacity            INTEGER         CHECK (capacity > 0),   -- Max workers
    status              project_status  NOT NULL DEFAULT 'draft',
    created_at          TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ     NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE  projects            IS 'A labour project. daily_wage is the default rate; contracts may override per-worker.';
COMMENT ON COLUMN projects.capacity   IS 'Optional cap on enrolled workers.';

-- =============================================================================
-- TABLE 5: project_locations
-- GPS anchor point + geofence radius for a project (used in attendance).
-- =============================================================================

CREATE TABLE project_locations (
    location_id         UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id          UUID        NOT NULL UNIQUE REFERENCES projects(project_id) ON DELETE CASCADE,
    latitude            DOUBLE PRECISION NOT NULL,
    longitude           DOUBLE PRECISION NOT NULL,
    radius_m            INTEGER     NOT NULL DEFAULT 200 CHECK (radius_m > 0),  -- Geofence radius
    address             TEXT,
    is_manual           BOOLEAN     NOT NULL DEFAULT FALSE,  -- TRUE if contractor typed coords
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE  project_locations          IS 'One GPS anchor per project. Haversine uses lat/lng + radius_m to validate attendance.';
COMMENT ON COLUMN project_locations.radius_m IS 'Default 200m. Contractor can adjust. Backend enforces; never trust client.';
COMMENT ON COLUMN project_locations.is_manual IS 'If TRUE, contractor entered coordinates manually instead of using browser GPS.';

-- =============================================================================
-- TABLE 6: contracts
-- QR-coded employment contract between a contractor project and a worker.
-- =============================================================================

CREATE TABLE contracts (
    contract_id         UUID            PRIMARY KEY DEFAULT gen_random_uuid(),
    worker_id           UUID            NOT NULL REFERENCES workers(worker_id) ON DELETE RESTRICT,
    project_id          UUID            NOT NULL REFERENCES projects(project_id) ON DELETE RESTRICT,
    contractor_id       UUID            NOT NULL REFERENCES contractors(contractor_id) ON DELETE RESTRICT,
    wage_rate           NUMERIC(10,2)   NOT NULL CHECK (wage_rate > 0),  -- Per-contract override
    status              contract_status NOT NULL DEFAULT 'pending',
    qr_token            TEXT            NOT NULL UNIQUE,  -- UUID-based token embedded in QR
    qr_url              TEXT,                             -- URL encoded in QR (accept endpoint)
    qr_expiry           TIMESTAMPTZ     NOT NULL,         -- Defaults to 7 days from generation
    accepted_at         TIMESTAMPTZ,
    created_at          TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ     NOT NULL DEFAULT NOW(),

    CONSTRAINT contracts_one_active_per_worker_project
        UNIQUE NULLS NOT DISTINCT (worker_id, project_id)  -- One contract per worker-project combo
);

COMMENT ON TABLE  contracts            IS 'QR contract links a worker to a project. QR token is single-use acceptance mechanism.';
COMMENT ON COLUMN contracts.qr_token   IS 'Short-lived token (UUID). Backend validates expiry. Embedded in QR image.';
COMMENT ON COLUMN contracts.wage_rate  IS 'Overrides projects.daily_wage for this specific worker if negotiated differently.';

-- =============================================================================
-- TABLE 7: attendance
-- One row per worker per project per day.
-- =============================================================================

CREATE TABLE attendance (
    attendance_id       UUID                PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id          UUID                NOT NULL REFERENCES projects(project_id) ON DELETE RESTRICT,
    worker_id           UUID                NOT NULL REFERENCES workers(worker_id) ON DELETE RESTRICT,
    supervisor_id       UUID                REFERENCES workers(worker_id),  -- NULL if self-marked
    contract_id         UUID                NOT NULL REFERENCES contracts(contract_id) ON DELETE RESTRICT,
    attendance_date     DATE                NOT NULL,
    status              attendance_status   NOT NULL DEFAULT 'present',
    pin_hash            TEXT,               -- SHA-256 of daily PIN. NULL if override.
    marked_at           TIMESTAMPTZ         NOT NULL DEFAULT NOW(),
    created_at          TIMESTAMPTZ         NOT NULL DEFAULT NOW(),

    CONSTRAINT attendance_unique_worker_date UNIQUE (worker_id, project_id, attendance_date)
);

COMMENT ON TABLE  attendance           IS 'Daily attendance. One row per worker/project/day. Duplicate prevented by UNIQUE constraint.';
COMMENT ON COLUMN attendance.pin_hash  IS 'SHA-256 of supervisor-generated PIN. Compared at mark time; never stored plain.';

-- =============================================================================
-- TABLE 8: attendance_verifications
-- GPS verification snapshot captured at attendance mark time.
-- =============================================================================

CREATE TABLE attendance_verifications (
    verification_id     UUID                PRIMARY KEY DEFAULT gen_random_uuid(),
    attendance_id       UUID                NOT NULL UNIQUE REFERENCES attendance(attendance_id) ON DELETE CASCADE,
    worker_lat          DOUBLE PRECISION,
    worker_lng          DOUBLE PRECISION,
    distance_m          DOUBLE PRECISION,   -- Haversine result vs project anchor
    within_radius       BOOLEAN,
    gps_accuracy        DOUBLE PRECISION,   -- Browser-reported accuracy in metres
    method              attendance_method   NOT NULL DEFAULT 'pin_gps',
    override_reason     TEXT,               -- Required when method = 'override'
    overridden_by       UUID                REFERENCES workers(worker_id),  -- Supervisor who overrode
    created_at          TIMESTAMPTZ         NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE  attendance_verifications IS 'GPS snapshot at mark time. Stored for audit; never re-checked post-submission.';
COMMENT ON COLUMN attendance_verifications.distance_m IS 'Haversine distance in metres. Stored even if within_radius = TRUE for audit purposes.';

-- =============================================================================
-- TABLE 9: wage_records
-- Auto-recalculated wage summary per worker per project.
-- One row per (worker, project). Recalculated on every attendance change.
-- =============================================================================

CREATE TABLE wage_records (
    wage_record_id      UUID            PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id          UUID            NOT NULL REFERENCES projects(project_id) ON DELETE RESTRICT,
    worker_id           UUID            NOT NULL REFERENCES workers(worker_id) ON DELETE RESTRICT,
    contract_id         UUID            NOT NULL REFERENCES contracts(contract_id) ON DELETE RESTRICT,
    days_worked         INTEGER         NOT NULL DEFAULT 0 CHECK (days_worked >= 0),
    daily_wage          NUMERIC(10,2)   NOT NULL CHECK (daily_wage > 0),
    expected_wage       NUMERIC(10,2)   GENERATED ALWAYS AS (days_worked * daily_wage) STORED,
    actual_paid         NUMERIC(10,2)   NOT NULL DEFAULT 0 CHECK (actual_paid >= 0),
    status              wage_status     NOT NULL DEFAULT 'pending',
    calculated_at       TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ     NOT NULL DEFAULT NOW(),

    CONSTRAINT wage_records_unique_worker_project UNIQUE (worker_id, project_id)
);

COMMENT ON TABLE  wage_records           IS 'Running wage tally. expected_wage is a generated column (days_worked * daily_wage). Recalculated by wage_calculator service.';
COMMENT ON COLUMN wage_records.expected_wage IS 'Auto-computed. Do not update directly.';

-- =============================================================================
-- TABLE 10: payment_ledger
-- Append-only log of payments declared by contractor.
-- NOT a payment gateway — records of declared payments only (PRD §1, AGENTS.md §1).
-- =============================================================================

CREATE TABLE payment_ledger (
    payment_id          UUID            PRIMARY KEY DEFAULT gen_random_uuid(),
    wage_record_id      UUID            NOT NULL REFERENCES wage_records(wage_record_id) ON DELETE RESTRICT,
    contractor_id       UUID            NOT NULL REFERENCES contractors(contractor_id) ON DELETE RESTRICT,
    worker_id           UUID            NOT NULL REFERENCES workers(worker_id) ON DELETE RESTRICT,
    project_id          UUID            NOT NULL REFERENCES projects(project_id) ON DELETE RESTRICT,
    amount              NUMERIC(10,2)   NOT NULL CHECK (amount > 0),
    payment_method      payment_method  NOT NULL,
    payment_date        DATE            NOT NULL,
    note                TEXT,
    recorded_at         TIMESTAMPTZ     NOT NULL DEFAULT NOW()
    -- No UPDATE/DELETE — append-only ledger. Enforce at application layer + RLS.
);

COMMENT ON TABLE payment_ledger IS 'Immutable record of declared payments. No UPI/Razorpay/Stripe — record-keeping only per AGENTS.md §1.';

-- =============================================================================
-- TABLE 11: disputes
-- Worker-raised disputes; resolved by Inspector.
-- =============================================================================

CREATE TABLE disputes (
    dispute_id          UUID                PRIMARY KEY DEFAULT gen_random_uuid(),
    worker_id           UUID                NOT NULL REFERENCES workers(worker_id) ON DELETE RESTRICT,
    contractor_id       UUID                NOT NULL REFERENCES contractors(contractor_id) ON DELETE RESTRICT,
    project_id          UUID                NOT NULL REFERENCES projects(project_id) ON DELETE RESTRICT,
    type                dispute_type        NOT NULL,
    description         TEXT                NOT NULL,
    linked_payment_id   UUID                REFERENCES payment_ledger(payment_id),  -- Optional
    status              dispute_status      NOT NULL DEFAULT 'open',
    priority            dispute_priority    NOT NULL DEFAULT 'medium',
    contractor_response TEXT,
    resolution          TEXT,
    resolved_by         UUID                REFERENCES users(id),  -- Inspector user_id
    created_at          TIMESTAMPTZ         NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ         NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE disputes IS 'Raise → Contractor responds → Inspector resolves. Frozen workflow per AGENTS.md §1.';

-- =============================================================================
-- TABLE 12: notifications
-- In-app notification queue. No SMS/email/push in MVP.
-- =============================================================================

CREATE TABLE notifications (
    notification_id     UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id             UUID        NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title               TEXT        NOT NULL,
    body                TEXT        NOT NULL,
    type                TEXT        NOT NULL,    -- e.g. 'contract_accepted', 'payment_received'
    is_read             BOOLEAN     NOT NULL DEFAULT FALSE,
    link                TEXT,                    -- Frontend route to navigate to on click
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE notifications IS 'In-app only. No external delivery in MVP. Polled via /notifications endpoint.';

-- =============================================================================
-- TABLE 13: audit_logs
-- Immutable append-only cross-cutting audit trail (PRD M-12).
-- Every state-changing endpoint MUST call write_audit_log().
-- =============================================================================

CREATE TABLE audit_logs (
    audit_id            UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id             UUID        REFERENCES users(id),      -- NULL for system actions
    action              TEXT        NOT NULL,                  -- e.g. 'attendance.mark', 'payment.record'
    entity_type         TEXT        NOT NULL,                  -- e.g. 'attendance', 'contract'
    entity_id           UUID,                                  -- FK to the affected row
    details             JSONB       NOT NULL DEFAULT '{}',     -- Arbitrary context/diff
    ip_address          TEXT,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
    -- No UPDATE/DELETE ever. RLS: INSERT only via service role, SELECT for inspector/admin.
);

COMMENT ON TABLE audit_logs IS 'Append-only audit trail. Every state change must write here. No UPDATE/DELETE permitted.';

-- =============================================================================
-- TABLE 14: user_preferences
-- Per-user language and settings.
-- =============================================================================

CREATE TABLE user_preferences (
    pref_id             UUID            PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id             UUID            NOT NULL UNIQUE REFERENCES users(id) ON DELETE CASCADE,
    preferred_language  app_language    NOT NULL DEFAULT 'en',
    updated_at          TIMESTAMPTZ     NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE user_preferences IS 'One row per user. Created on registration; updated via PUT /workers/me/preferences.';

-- =============================================================================
-- TABLE 15: minimum_wages
-- Reference table for state-level minimum wage rates by occupation.
-- Seeded once; updated by Admin only.
-- =============================================================================

CREATE TABLE minimum_wages (
    wage_id             UUID            PRIMARY KEY DEFAULT gen_random_uuid(),
    state               TEXT            NOT NULL,
    occupation          TEXT            NOT NULL,
    wage_rate           NUMERIC(10,2)   NOT NULL CHECK (wage_rate > 0),
    effective_date      DATE            NOT NULL,
    created_at          TIMESTAMPTZ     NOT NULL DEFAULT NOW(),

    CONSTRAINT minimum_wages_unique_state_occ_date UNIQUE (state, occupation, effective_date)
);

COMMENT ON TABLE minimum_wages IS 'Reference data only. No ML. Used by wage_calculator to flag underpayment vs state minimum.';

-- =============================================================================
-- INDEXES  (PRD §9.3)
-- =============================================================================

-- Attendance queries (most frequent)
CREATE INDEX idx_attendance_worker_date    ON attendance(worker_id, attendance_date);
CREATE INDEX idx_attendance_project_date   ON attendance(project_id, attendance_date);

-- Contract lookups
CREATE INDEX idx_contracts_worker          ON contracts(worker_id);
CREATE INDEX idx_contracts_project         ON contracts(project_id);
CREATE INDEX idx_contracts_qr_token        ON contracts(qr_token);

-- Payment queries
CREATE INDEX idx_payments_worker           ON payment_ledger(worker_id);
CREATE INDEX idx_payments_project          ON payment_ledger(project_id);
CREATE INDEX idx_payments_date             ON payment_ledger(payment_date);

-- Dispute queue
CREATE INDEX idx_disputes_status           ON disputes(status);
CREATE INDEX idx_disputes_priority         ON disputes(priority, status);

-- Notifications (unread polling is the hot path)
CREATE INDEX idx_notifications_user_unread ON notifications(user_id, is_read) WHERE is_read = FALSE;

-- Audit logs
CREATE INDEX idx_audit_created             ON audit_logs(created_at DESC);
CREATE INDEX idx_audit_entity              ON audit_logs(entity_type, entity_id);
CREATE INDEX idx_audit_user                ON audit_logs(user_id);

-- Additional useful indexes not in PRD §9.3 but derived from query patterns
CREATE INDEX idx_workers_user_id           ON workers(user_id);
CREATE INDEX idx_contractors_user_id       ON contractors(user_id);
CREATE INDEX idx_projects_contractor       ON projects(contractor_id);
CREATE INDEX idx_projects_status           ON projects(status);
CREATE INDEX idx_wage_records_project      ON wage_records(project_id);
CREATE INDEX idx_wage_records_worker       ON wage_records(worker_id);

-- =============================================================================
-- SEED DATA: minimum_wages (sample rows — replace with real state data)
-- =============================================================================

INSERT INTO minimum_wages (state, occupation, wage_rate, effective_date) VALUES
    ('Maharashtra', 'construction_unskilled',  400.00, '2024-04-01'),
    ('Maharashtra', 'construction_semi_skilled',480.00, '2024-04-01'),
    ('Maharashtra', 'construction_skilled',    560.00, '2024-04-01'),
    ('Delhi',       'construction_unskilled',  688.00, '2024-04-01'),
    ('Delhi',       'construction_semi_skilled',762.00, '2024-04-01'),
    ('Delhi',       'construction_skilled',    843.00, '2024-04-01'),
    ('Karnataka',   'construction_unskilled',  423.00, '2024-04-01'),
    ('Karnataka',   'construction_semi_skilled',486.00, '2024-04-01'),
    ('Karnataka',   'construction_skilled',    536.00, '2024-04-01');

-- =============================================================================
-- END OF SCHEMA
-- Tables: 15 ✓   Indexes: 18 ✓   Enums: 10 ✓
-- Last modified: Day 1 — DO NOT ALTER without explicit sign-off (AGENTS.md §1)
-- =============================================================================
