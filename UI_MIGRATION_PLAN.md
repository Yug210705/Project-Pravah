# UI Migration Plan — PRAVAH

## 1. Existing Frontend Framework
- Pure HTML, CSS, and vanilla JavaScript embedded inside Jinja2 templates (e.g., `dashboard.html`).
- No SPA frameworks (React/Vue) or bundlers are currently used.

## 2. Current Root Entry & Gateway Architecture
- The root entry is `gateway.py` (FastAPI), which acts as a reverse proxy, WebSocket bridge, and process supervisor.
- It binds to `:5000` and directly serves `dashboard.html` for the `/` route via a static `FileResponse`.
- Five underlying microservices run on internal ports (15001-15005).
- `gateway.py` handles API dispatch via intelligent path prefix matching (`/api/*`).

## 3. Current Routing & Module URLs
- **Dashboard:** `/`
- **Module 1 (NLP):** `/module1` (Static UI mock)
- **Module 2 (Geospatial/AHP):** `/module2/*`
- **Module 3 (Telemetry Monitor):** `/module3/monitor`, `/module3/outputs/*`
- **Module 4 (GraphRAG):** `/module4/*`
- **Module 5 (Engineering Agent):** `/module5/*`

## 4. Existing CSS & Theme System
- The existing UI uses a dark, "cyberpunk/tactical" aesthetic (e.g., `#0d1117`, `#00e5ff`, `#58a6ff`, `#3fb950`).
- Matrix-style binary rain canvas animations.
- Hacker-terminal window styling for the dashboard.
- No central CSS design token file. Styles are hardcoded inline in `<style>` blocks inside each template.

## 5. Existing Logos & Assets
- No official `OIL` (Oil India Limited) logo in the `assets/` directory (only screenshots and custom icons).
- Will create a clean text-based placeholder `OIL | Oil India Limited` as requested.
- `assets/` folder contains app screenshots (`main_dash.png`, `module_2.png`, etc.).

## 6. Existing Reusable Components
- Minimal reuse. Each module is largely a standalone HTML file with its own DOM structure and inline styles.

## 7. API Endpoints
- **M2 (Geo/AHP):** `/api/wells`, `/api/analogs`, `/api/formation`, `/api/well/*`
- **M3 (Telemetry):** `/api/telemetry/*`, `/api/anomaly/*`, `/ws/telemetry`, `/ws/anomaly`
- **M4 (Graph):** `/api/graph/*`, `/api/rag/*`, `/api/briefing/*`, `/api/backtest`
- **M5 (Agent):** Handled internally or exposed via specific routes

## 8. Migration Strategy (Phased Approach)

**Phase 1: Audit & Prep (Current)**
- Completed the audit. Documenting findings here.

**Phase 2: Global Application Shell (Next Step)**
- Create a central `layout.html` or update `dashboard.html` to act as the SPA or iframe-based shell wrapper.
- Given the current architecture uses separate endpoints serving full HTML pages, the most seamless way to preserve backend logic while giving an SPA feel is to either:
  1. Build a global shell with an `iframe` that loads the module routes.
  2. Rewrite the frontend to be a true SPA (e.g., fetch and render).
  3. Inject a standard header/sidebar component into every Flask template.
- *Decision:* A central `layout.html` (Jinja2 macro) injected into all existing pages, or a top-level shell that loads module contents via AJAX/iframes to preserve state without full page reloads.

**Phase 3: Dashboard Restyling**
- Remove hacker aesthetic.
- Implement the "Enterprise Overview" (KPI row, active wells, risks, events).

**Phase 4: Module-by-Module Restyling**
- Restyle M2 (Map/AHP), M3 (Telemetry Monitor), M4 (Graph), M5 (Agent) to use the unified light theme.

**Phase 5: Polish & Consistency**
- Add empty states, error handling, typography (Inter), spacing, and responsive checks.
