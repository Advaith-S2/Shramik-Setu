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
| 9 | Disputes | M-09 | Raise → respond → resolve flow complete with audit trail |
| 10 | Inspector Dashboard + Audit Log | M-10, M-12 | Charts render, dispute queue works, audit log filterable |
| 11 | Notifications + i18n | M-11, M-13 | In-app notifications fire on all triggers; EN/HI/MR switch works |
| 12 | Integration + testing + demo polish | all | E2E flow rehearsed 3x, no P0 bugs, demo script walkthrough clean |

You will very likely need more than 12 sessions given usage limits — that's
fine. Treat each row as a *milestone*, not a literal single sitting. Split
a row across 2 sessions if needed and just update Current State mid-row.

---

## Current State
*(update this section every session — this is the single source of truth)*

**Last updated:** 2026-08-05
**Day/Phase reached:** Day 1 — Repo scaffold, backend routers/services, Supabase schema live, frontend setup complete.
**What works right now:**
- FastAPI backend scaffold with all endpoints stubbed out
- Backend health tests passing
- Supabase schema with 15 tables created
- Frontend Next.js scaffold initialized with shadcn/ui and TailwindCSS
- Frontend routes stubbed out for all user roles
- Environment placeholders `.env.example` and `.env.local.example` created

**Known gaps / deferred items:**
- Auth integration (Day 2)
- External backend deployment (Next session)

---

## Next Up
*(the very first thing the next session should do — be specific)*

- Finish Render deploy for FastAPI backend, verify /health endpoint responds, then start M-01 auth (Day 2)

---

## Deviations from PRD / schema / API spec
*(anything you changed from the original plan, and why — keeps future
sessions from "fixing" it back)*

| Date | Deviation | Reason |
|---|---|---|
| 2026-08-05 | Changed `Geist` font to `Inter` | `Geist` font failed to resolve via `next/font/google` in Next.js 14.2.35. |

---

## Session Log

### Session 1 — 2026-08-05
- **Model(s) used:** Gemini 3.1 Pro (Low)
- **Goal:** Finish Day 1 project setup
- **Done:** Completed Next.js scaffold, fixed lint and build errors, initialized shadcn/ui, created environment file placeholders, verified backend health check.
- **Blockers:** None
- **Next:** Proceed with Day 2 - Auth integration and backend deployment.
