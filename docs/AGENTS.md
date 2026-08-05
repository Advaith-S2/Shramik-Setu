# AGENTS.md — ShramikSetu

Rules for any AI coding agent (Antigravity, Claude Code, Cursor, etc.) working
in this repo. Read this before writing any code. If something here conflicts
with your own instinct for "best practice," follow this file — scope
discipline matters more than elegance on a 12-week academic MVP.

---

## 0. Before touching code, read in this order
1. `PROGRESS.md` — what's already built, what's next, any deviations
2. `docs/PRD.md` — Section 8 (Module Specs) for the module you're building
3. `docs/schema.sql` — do not invent tables/columns not listed here
4. `docs/API_SPEC.md` — do not invent endpoints not listed here

If a task isn't covered by these, stop and ask rather than improvising.

---

## 1. Hard constraints — never do these
- **No AI/ML of any kind.** No sentiment analysis, no "smart" scoring, no
  LLM calls, no recommendation logic. If a feature smells like ML, it's out
  of scope (see PRD §2.4, §6 Won't-Have).
- **No real payment gateway.** Payment Ledger is insert-only records of
  declared payments, not money movement. Never add UPI/Razorpay/Stripe.
- **No Aadhaar, biometrics, SMS gateway, blockchain, native mobile app.**
- **No continuous/background GPS tracking.** Location is captured once,
  only during attendance marking.
- **Don't modify the frozen workflow**: Contract → QR → Attendance → Wage →
  Payment → Passport → Dispute. Don't reorder or merge these steps.
- **Don't touch `docs/schema.sql` after Day 1** without explicit sign-off.
  Schema changes cascade into every module.

## 2. Tech stack — do not substitute
| Layer | Choice | Do not swap for |
|---|---|---|
| Frontend | Next.js 14 (App Router), TypeScript, TailwindCSS, shadcn/ui | Vite, Remix, plain CSS, Chakra/MUI |
| State | React Server Components + SWR | Redux, Zustand (unless a screen genuinely needs local complex state — ask first) |
| i18n | next-intl, static JSON | react-i18next, AI-translated strings |
| Backend | FastAPI (Python 3.11+) | Express, Django, Flask |
| DB | PostgreSQL via Supabase | Mongo, Firebase |
| Auth | Supabase Auth (email+password, JWT) | Auth0, custom auth server, NextAuth |
| PDF | ReportLab | Puppeteer/HTML-to-PDF, WeasyPrint |
| QR | `qrcode` (Python) | Client-side JS QR libs |
| Charts | Chart.js | Recharts, D3 (unless explicitly told) |
| Hosting | Vercel (FE) + Render (BE) + Supabase (DB) | AWS, unless a session explicitly says "AWS phase" |

## 3. Module ownership (see PRD §16.3) — stay in your lane
- **Dev 1 lane**: Auth, Worker Profile, Attendance, Payment Ledger
- **Dev 2 lane**: Projects, QR Contracts, GPS/Haversine, Inspector Dashboard
- **Dev 3 lane**: Worker Dashboard, Passport PDF, Dispute UI, E2E tests
- **Dev 4 lane**: Supervisor Dashboard, Notifications, Audit Log, i18n, CI/CD

When starting an Antigravity session, tell the agent which lane/module
you're in *today* so it doesn't wander into files owned by a later phase.

## 4. Coding conventions
- API routes: `/api/v1/<resource>`, plural nouns, REST verbs per PRD §10.1
- Every state-changing endpoint calls `write_audit_log(...)` — see PRD M-12
- Every user-facing string goes through the translation key system, never
  hardcoded — see PRD M-13
- Backend folder structure: `routers/`, `services/`, `models/`, `schemas/`,
  `middleware/` exactly as laid out in PRD §7.2
- Pydantic models validate every request; never trust client input
- New DB migrations go in `backend/migrations/`, never raw ALTER in prod

## 5. Testing expectation
- Every new endpoint gets at least one pytest happy-path + one error-case test
- Don't skip tests to save time — flag it in `PROGRESS.md` instead if you
  genuinely must defer, so it isn't forgotten

## 6. End-of-session checklist (do this every time, no exceptions)
1. Code compiles / app boots locally
2. Commit with a clear message referencing the module (e.g. `M-05: PIN attendance backend`)
3. Update `PROGRESS.md`:
   - What got done today
   - What's next
   - Any deviation from PRD/schema/API spec, with reason
4. Do NOT leave half-written features uncommitted — commit working
   increments even if the module isn't 100% done; note the gap in PROGRESS.md

## 7. Model selection inside Antigravity (see PROGRESS.md §Model Guide)
Use a stronger/reasoning-tier model for: schema design, API contract design,
GPS/Haversine logic, wage calculation logic, RBAC/security middleware,
dispute state machine.

Use a faster/lighter-tier model for: CRUD scaffolding, form UI, translation
JSON population, shadcn/ui component wiring, repetitive boilerplate across
similar screens.

Always re-check the actual model list in Antigravity's picker — names and
availability change; this file only specifies capability tier, not a
specific model name.
