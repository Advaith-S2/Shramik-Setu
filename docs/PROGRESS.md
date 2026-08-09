# PROGRESS.md — ShramikSetu Build Log

Update this file at the **end of every Antigravity session**, no exceptions.
Next session (today or tomorrow) starts by reading this file first.

---

## How to use this file
1. Before starting: read "Current State" + "Next Up"
2. Tell Antigravity which day/module you're working on (see phase plan)
3. Pick a model per the tier guide below for the task type
4. At session end: fill in today's entry in the Session Log, update
   "Current State" and "Next Up"

---

## Model tier guide for Antigravity

Antigravity's model list changes — check the picker for current names.
Map today's task to a tier, then pick whatever fills that tier right now.

| Tier | Use for | Why |
|---|---|---|
| **Reasoning / strongest available** | Schema design, API contract design, Haversine + wage calc logic, RBAC middleware, dispute state machine, anything touching money or security | These bugs are expensive to find later; correctness matters more than speed |
| **Balanced / mid-tier** | Endpoint implementation once contract is fixed, service-layer logic, integration between modules | Good reasoning-to-speed tradeoff for "implement this known spec" work |
| **Fast / lightweight** | CRUD scaffolding, shadcn/ui component wiring, form UI, repetitive screens (e.g. 4 nearly-identical dashboard cards), translation JSON population, boilerplate tests | High volume, low ambiguity — speed matters more than depth |

Rule of thumb: if you'd need to double-check the agent's output carefully
by hand anyway, use the strongest tier and save yourself the review time.
If the task is "do this 10 similar times," use the fast tier and just skim.

---

## Phase plan (12 sessions, adjust to your actual pace/limits)

| Day | Focus | Modules | Ends when... |
|---|---|---|---|
| 1 | Repo scaffold + Supabase schema + local dev | infra | Frontend + backend run locally, Supabase schema (15 tables) live, `.env` files working |
| 2 | Auth + deploy pipeline | M-01 | Register/login works for all 4 roles locally, THEN deploy to Vercel/Render so first deploy = working auth, not a blank page |
| 3 | Worker + Contractor profiles | M-02, M-03 (shell) | Profile CRUD works both sides, photo upload works |
| 4 | Projects + QR Contracts | M-03 (full), M-04 | Contractor creates project → QR generates → worker scans & accepts |
| 5 | Attendance + GPS | M-05, M-14 | PIN generation + Haversine GPS check marks attendance end-to-end |
| 6 | Wage calculator | M-06 | Wage auto-recalculates on every attendance change, shown on both dashboards |
| 7 | Payment Ledger | M-07 | Contractor records payment, worker sees it, wage status updates |
| 8 | Employment Passport PDF | M-08 | PDF downloads with correct data incl. Devanagari rendering test |
| 9-10 | Disputes, Inspector + Wallet (Sprint 5) | M-09, M-10, M-12, M-15 | Full dispute flow, charts render, audit log, Wallet active. *Week 9 midpoint checkpoint: cut District Analytics first if behind schedule.* |
| 11 | Notifications + i18n | M-11, M-13 | In-app notifications fire on all triggers; EN/HI/MR switch works |
| 12 | Integration + testing + demo polish | all | E2E flow rehearsed 3x, no P0 bugs, demo script walkthrough clean |

You will very likely need more than 12 sessions given usage limits — that's
fine. Treat each row as a *milestone*, not a literal single sitting. Split
a row across 2 sessions if needed and just update Current State mid-row.

---

## Current State
*(update this section every session — this is the single source of truth)*

**Last updated:** 2026-08-09
**Day/Phase reached:** Day 1 — Complete and stable (repo scaffold, Supabase schema with 15 tables, frontend/backend running locally).
**What works right now:**
- FastAPI backend scaffold with all endpoints stubbed out
- Backend health tests passing
- Supabase schema with 15 tables live
- Frontend Next.js scaffold initialized with shadcn/ui and TailwindCSS
- Frontend routes stubbed out for all user roles
- Environment placeholders `.env.example` and `.env.local.example` created
- Supabase clients for both frontend and backend successfully connected to a live database
- PRD updated to add Digital Wage Wallet (M-15) — see PRD.md's Scope Validation section for the Sprint 5 impact and Week 9 checkpoint.

**Known gaps / deferred items:**
- Auth integration (Day 2). A first attempt at Day 2 (M-01 Auth) was made and hit two real bugs (Supabase ES256 JWT verification incompatible with local decode, and sync/async event-loop blocking with the Supabase Python client) that were diagnosed but not cleanly resolved within that session. The repo was reverted to a clean Day 1 state via the day1-backup branch. Auth is currently NOT implemented — routers/middleware are back to stub state.
- External backend deployment (Day 2)

---

## Next Up
*(the very first thing the next session should do — be specific)*

- Restart Day 2 (M-01 Auth) fresh, using the corrected approach that pre-specifies: (1) verify JWT via supabase.auth.get_user() not local decode, since Supabase issues ES256 asymmetric tokens; (2) define auth-related FastAPI handlers as sync def not async def since the Supabase Python client is synchronous; (3) build backend fully first, verify via pytest and Swagger UI, pause; (4) build frontend, pause; (5) manually verify full flow locally before any commit; (6) finally, finish Render deploy for FastAPI backend once local Auth is fully verified.

---

## Deviations from PRD / schema / API spec
*(anything you changed from the original plan, and why — keeps future
sessions from "fixing" it back)*

| Date | Deviation | Reason |
|---|---|---|
| 2026-08-05 | Changed `Geist` font to `Inter` | `Geist` font failed to resolve via `next/font/google` in Next.js 14.2.35. |
| 2026-08-09 | Day 2 Auth reverted after ES256/async bugs, restarting with documented fixes | Avoid repeating the same debugging cycle; root causes now known and specified upfront. |

---

## Session Log

### Session 2 — 2026-08-09
- **Model(s) used:** Antigravity Reasoning
- **Goal:** Update PRD for Digital Wage Wallet (M-15), attempt Auth (M-01)
- **Done:** PRD updated with Wallet (M-15). Day 2 Auth attempted and reverted due to the two bugs (ES256 verification and async blocking). Repo restored to clean state on main via day1-backup branch merge.
- **Blockers:** None currently; bugs were diagnosed and fixes documented.
- **Next:** Restart Day 2 (M-01 Auth) fresh with the corrected approach.

### Session 1 — 2026-08-05
- **Model(s) used:** Gemini 3.1 Pro (Low)
- **Goal:** Finish Day 1 project setup
- **Done:** Completed Next.js scaffold, fixed lint and build errors, initialized shadcn/ui, created environment file placeholders, verified backend health check.
- **Blockers:** None
- **Next:** Proceed with Day 2 - Auth integration and backend deployment.
