# 🚨 CrowAgent™ Platform — BCP Rebuild Guide
**Business Continuity / Disaster Recovery — Complete Rebuild Using Claude Code**

> Your single source of truth for rebuilding CrowAgent™ from zero using Claude Code.
> Follow phases in order. Each phase ends with a human approval checkpoint.

**Time estimate:** 4–8 hours with Claude Code
**Prerequisites:** GitHub account, Python 3.11+, Gemini API key (free), VS Code + Claude Code

---

## Repository Reference
- **Original:** https://github.com/WonderApri/crowagent-platform
- **Fork:** https://github.com/parihab/crowagent-platform
- **Stack:** Python 3.11 · Streamlit · Google Gemini 1.5 Flash · Open-Meteo API · PINN thermal model
- **AI used in development:** Claude Code (Anthropic)

---

## Phase 0 — Environment Setup

```bash
npm install -g @anthropic-ai/claude-code   # Install Claude Code
git clone https://github.com/WonderApri/crowagent-platform.git
cd crowagent-platform
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # Add your keys
```

> ✅ **HUMAN CHECKPOINT 0:** Run `streamlit run app/main.py` — UI must load before proceeding.

---

## Phase 1 — Context Loading

**Claude Code prompt:**
```
Read /prompts/01_CONTEXT.md and confirm you understand the full platform context,
architecture, and constraints before I give you any tasks.
```

> ✅ **HUMAN CHECKPOINT 1:** Review Claude's summary. Correct any misunderstandings.

---

## Phase 2 — Requirements Specification (Team 1)

**Claude Code prompt:**
```
Read /prompts/02_SPECIFICATION_AGENT.md and produce a complete requirements
specification for CrowAgent™. Output as REQUIREMENTS_SPEC.md. No code yet.
```

> ✅ **HUMAN CHECKPOINT 2:** Review and annotate before proceeding.

---

## Phase 3 — Architecture Review (Team 1)

**Claude Code prompt:**
```
Read /prompts/03_ARCHITECTURE_REVIEW_AGENT.md. Review the repo and produce
ARCHITECTURE_ASSESSMENT.md.
```

> ✅ **HUMAN CHECKPOINT 3:** Approve architecture before any code is written.

---

## Phase 4 — Core Platform Rebuild (Team 2)

Run in sequence:

### 4a. Scaffold structure
```
Read /prompts/00_PRE_EXECUTION_PROMPT.md first. Then scaffold the full directory
structure as described in /prompts/01_CONTEXT.md. Create empty module files with
docstrings only. Do not implement logic yet.
```

### 4b. Rebuild thermal model
```
Implement core/thermal_model.py using PINN methodology (Raissi et al., 2019).
Use BEIS 2023 emission factor 0.20482 kgCO₂e/kWh. Cite every constant from spec.
```

### 4c. Rebuild financial engine
```
Implement core/financial_engine.py. Include NPV, IRR, payback period, ROI,
cost-per-tonne CO₂. Reference REQUIREMENTS_SPEC.md. Do not modify formulas
without my explicit approval.
```

### 4d. Rebuild services
```
Implement services/weather_service.py using Open-Meteo API (free, no key).
Implement services/gemini_service.py for Gemini 1.5 Flash. Load keys from
.streamlit/secrets.toml or .env only — never hardcode.
```

### 4e. Rebuild UI
```
Implement app/main.py as Streamlit entry point. Build dashboard, financial
analysis, AI advisor, and portfolio management tabs. Reference 01_CONTEXT.md.
```

> ✅ **HUMAN CHECKPOINT 4:** Run `streamlit run app/main.py`. Verify all tabs. Verify financial outputs match spec.

---

## Phase 5 — Security & Testing (Team 2)

**Claude Code prompt:**
```
Read /prompts/04_DEVSECOPS_AGENT.md. Generate full test suite in tests/.
Run bandit and flake8. Report findings. Do NOT modify application logic
to fix failures — report to me first.
```

> ✅ **HUMAN CHECKPOINT 5:** Review results. Approve all fixes before applying.

---

## Phase 6 — E2E Validation (Team 3)

**Claude Code prompt:**
```
Read /prompts/05_E2E_VALIDATION_AGENT.md. Simulate full user flow.
Produce a validation report. Do not auto-fix failures without my approval.
```

> ✅ **HUMAN CHECKPOINT 6:** All E2E items must pass before deployment.

---

## Phase 7 — Deployment (Team 3)

**Claude Code prompt:**
```
Read /prompts/06_DEPLOYMENT_GOVERNANCE.md. Confirm all checklist items.
Prepare .github/workflows/ci.yml.
```

```bash
git add .
git commit -m "feat: full platform rebuild via Claude Code BCP"
git push origin main
```

> ✅ **HUMAN CHECKPOINT 7 (FINAL):** CI must be green on GitHub Actions before merge.

---

## Rebranding for a New Organisation

```
I want to rebrand this platform for [Organisation Name].
Replace:
- "CrowAgent™" → "[Your Platform Name]"
- "Greenfield University" → "[Your Institution Name]"
- Contact email → "[Your email]"
- Copyright notice → "[Your Name], [Year]"

Do NOT change any financial formulas, emission factors, or physics model logic.
List every file you will modify. Wait for my approval before making changes.
```

> ⚠️ CrowAgent™ is a trademark of Aparajita Parihar. Remove all branding when deploying for your own organisation.

---

## Quick Reference

| File | Purpose | Team |
|------|---------|------|
| `prompts/00_PRE_EXECUTION_PROMPT.md` | Agent guardrails | All |
| `prompts/01_CONTEXT.md` | Platform context | All |
| `prompts/02_SPECIFICATION_AGENT.md` | Requirements | Team 1 |
| `prompts/03_ARCHITECTURE_REVIEW_AGENT.md` | Architecture | Team 1 |
| `prompts/04_DEVSECOPS_AGENT.md` | Security + tests | Team 2 |
| `prompts/05_E2E_VALIDATION_AGENT.md` | E2E validation | Team 3 |
| `prompts/06_DEPLOYMENT_GOVERNANCE.md` | Deployment | Team 3 |
| `governance/MANIFEST.md` | Non-negotiables | All |
| `governance/OPERATING_MODEL.md` | 3-team model | All |
| `claude-sdlc/CLAUDE_CODE_SDLC.md` | Claude Code story | Reference |

*v1.0 · March 2026 · Maintained by Aparajita Parihar*
