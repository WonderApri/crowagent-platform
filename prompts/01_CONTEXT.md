# CrowAgent™ Platform — Full Context Document

**Load this before any technical task.**

---

## Platform Purpose

CrowAgent™ is a physics-informed campus thermal intelligence system for
university estate managers. It enables evidence-based, cost-effective decisions
for achieving Net Zero targets.

**Key outputs:** Energy savings, CO₂ reduction, NPV, IRR, payback period,
cost-per-tonne CO₂, AI-generated retrofit recommendations.

---

## Repository Structure

```
crowagent-platform/
├── app/                    # Streamlit UI entry point (app/main.py)
├── core/                   # Physics engine + financial engine
│   ├── thermal_model.py    # PINN thermal model (Raissi et al., 2019)
│   └── financial_engine.py # NPV, IRR, payback, ROI calculations
├── services/               # External API integrations
│   ├── weather_service.py  # Open-Meteo API (free)
│   └── gemini_service.py   # Google Gemini 1.5 Flash AI Advisor
├── config/                 # Platform constants and settings
├── governance/             # Governance rules and manifest
├── prompts/                # Claude Code prompt files (this folder)
├── tests/                  # pytest test suite
├── assets/                 # Logo and brand assets
├── .streamlit/             # Streamlit config and secrets
├── .github/workflows/      # GitHub Actions CI
└── requirements.txt        # Python dependencies
```

---

## Architecture Principles

- **UI layer (app/):** Display only. No business logic.
- **Core layer (core/):** All physics and financial calculations. Stateless.
- **Services layer (services/):** External API calls only. Isolated and mockable.
- **Config layer (config/):** All constants. Single source of truth for values.
- **Session state:** Managed in app/ only. Keys must be documented.

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| UI framework | Streamlit |
| Language | Python 3.11 |
| AI Advisor | Google Gemini 1.5 Flash |
| Weather data | Open-Meteo API (free, no key) |
| Optional weather | Met Office DataPoint (free key) |
| Physics model | PINN (Raissi et al., 2019) |
| Testing | pytest |
| Security scan | bandit, pip-audit |
| Lint | flake8 |
| CI/CD | GitHub Actions |

---

## Source-Locked Constants

**Do not change these without a spec update and human approval:**

| Constant | Value | Source |
|----------|-------|--------|
| Grid carbon intensity | 0.20482 kgCO₂e/kWh | BEIS GHG 2023 |
| UK HE electricity | £0.28/kWh | HESA 2022-23 |
| Heating season | 5,800 hrs/yr | CIBSE Guide A |
| Solar irradiance (Reading) | 950 kWh/m²/yr | PVGIS EC JRC |

---

## Secrets Management

- Gemini API key: `GEMINI_KEY` in `.streamlit/secrets.toml` or `.env`
- Met Office key: `MET_OFFICE_KEY` in `.streamlit/secrets.toml` or `.env`
- Never commit `.env` or `.streamlit/secrets.toml`
- `.env.example` is the safe template

---

## Demonstration Data

- **Fictional institution:** Greenfield University (not a real place)
- Default portfolio contains demo buildings for illustration only
- All financial results are indicative — not for capital investment decisions

---

## Intellectual Property

- Copyright © 2026 Aparajita Parihar
- CrowAgent™ trademark pending (UK IPO Class 42)
- Contact: crowagent.platform@gmail.com
