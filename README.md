# Aegis · AI governance workspace

A polished, self-contained MVP for governing artificial intelligence inside an organisation. Aegis gives a governance team one place to register AI systems, score their risk, attest to policies, respond to incidents, record human approvals, and keep an audit trail.

Everything runs in the browser. There is no build step, no package manager, and no backend. Demo data is stored in `localStorage`, and the workspace can be reset at any time from **Settings**.

---

## Run it

**Windows**

- Double-click `run.bat`, or
- Right-click `run.ps1` → *Run with PowerShell*, or
- From a terminal:

```powershell
python serve.py
```

**macOS / Linux**

```sh
./run.sh
```

The launcher starts a local static server on the first free port from `8000` and opens `http://localhost:8000/`. You can pass a port explicitly: `python serve.py 8080`.

Any static server works. Opening `index.html` directly from disk will not work because the app uses ES modules.

---

## What is included

| Area | Capability |
| --- | --- |
| **Overview** | Governance health score, attention queue, KPI strip, risk distribution, incidents, policy coverage, review calendar, recent activity |
| **AI systems** | Full inventory, lifecycle status, ownership, risk tier, filtering/search, CSV export, detail record with overview, risk posture, policies, incidents, reviews, and audit history |
| **Risk assessments** | Weighted factor scoring, six compensating controls, residual score, classification, assessment history, assessment record modal |
| **Policies** | Policy library, drafts and publishing, category filters, per-system attestation, coverage tracking, retire/publish flows |
| **Incidents** | Severity-based response SLAs, incident register, filtering, status workflow with containment notes, CSV export |
| **Approvals** | Review requests, pending queue, decision history, approve/reject with mandatory rejection rationale |
| **Audit trail** | Append-only event log, actor/action/category filters, CSV export |
| **Settings** | Organisation profile, frameworks, user profile, JSON export, demo reset, clear governance records |

### Risk model

The MVP combines a simplified **EU AI Act use-case classification** with a quantitative residual risk score.

- **Regulatory tier** — derived from the selected use case: prohibited, high, limited, or minimal risk.
- **Inherent risk (0–12)** — four factors worth 0–3 points each:
  - data sensitivity
  - decision autonomy
  - affected population
  - external exposure
- **Residual risk** — each of six documented controls reduces the score by 1 point:
  - human oversight & escalation
  - bias & fairness testing
  - monitoring & drift detection
  - explainability documentation
  - data protection impact assessment
  - security & red-team review

Residual levels: **Low** (0–2), **Moderate** (3–5), **Elevated** (6–8), **Critical** (9–12).

Review cadence defaults: high/prohibited every 90 days, limited every 180 days, minimal annually.

> This is a demonstration MVP. It is not legal advice and does not replace a formal compliance programme.

---

## Demo workspace

The seed data represents **Northwind Group**, a fictional financial services organisation, with:

- 11 AI systems across production, pilot, development, and retired states
- 9 completed risk assessments
- 7 policies with mixed attestation coverage
- 6 incidents, including critical and SLA-breaching examples
- 6 approval reviews
- A populated audit trail

Use **Settings → Reset demo data** to restore the original workspace after experimenting.

---

## Project structure

```text
aegis-ai-governance/
├── index.html              App shell and static asset loading
├── serve.py                Zero-dependency local preview server
├── run.bat / run.ps1       Windows launchers
├── run.sh                  macOS / Linux launcher
├── assets/
│   ├── styles.css          Design tokens, shell, navigation, dashboard
│   ├── components.css      Tables, forms, detail views, modals
│   └── responsive.css      Breakpoints and print styles
└── src/
    ├── app.js              Boot, chrome, routing, search, notifications
    ├── router.js           Hash router
    ├── store.js            State, persistence, selectors, mutations
    ├── seed.js             Northwind Group demo data
    ├── risk.js             Risk model and use-case catalogue
    ├── ui.js               Icons, badges, charts, forms, modals, toasts
    ├── actions.js          Register / assess / report / approve flows
    └── views/              One module per workspace area
```

## Notes

- **Persistence:** state is saved under the `aegis.governance.v1` key in `localStorage`. Nothing leaves the browser.
- **Routing:** hash-based (`#/systems`, `#/systems/sys_...`, `#/policies`, etc.), so the app works from any static host.
- **Browser support:** current Chrome, Edge, Firefox, and Safari. CSS uses `:has()` for checked custom controls; the inputs remain functional without it.
- **Accessibility:** semantic tables and forms, visible focus states, labelled dialogs with focus trapping and focus restoration, `aria-live` toasts, keyboard-operable row navigation, and reduced-motion support.

## Resetting manually

Open DevTools and run:

```js
localStorage.removeItem("aegis.governance.v1");
location.reload();
```
