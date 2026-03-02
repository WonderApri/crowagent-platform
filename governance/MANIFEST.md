# CrowAgent™ Platform — Engineering Manifest

## Mission
Deliver a deterministic, physics-accurate, financially rigorous sustainability
advisory platform for university estate management. Enable evidence-based
Net Zero decision-making without hallucinated outputs.

## Non-Negotiables
- No hallucinated code, constants, or financial values
- No undocumented logic
- No silent dependency additions — all packages must be in requirements.txt
- No modification of thermal model, financial formulas, or emission factors
  without a corresponding spec update and human approval
- All API calls must handle failure gracefully
- All secrets loaded from .streamlit/secrets.toml or .env — never hardcoded
- No direct push to main branch — pull requests mandatory

## Architecture Guardrails
- Streamlit-based UI — no framework migration without Team 1 approval
- `core/` is the physics and financial engine — UI must not contain logic
- `services/` handles all external API calls — no direct API calls from UI
- `config/` owns all platform constants — no magic numbers elsewhere
- Session state keys are documented — adding new keys requires approval
- BEIS 2023 emission factor: **0.20482 kgCO₂e/kWh** — do not change
- UK HE electricity cost: **£0.28/kWh** — do not change without HESA citation

## Emission & Financial Constants (Source-Locked)
| Constant | Value | Source |
|----------|-------|--------|
| Grid carbon intensity | 0.20482 kgCO₂e/kWh | BEIS GHG Conversion Factors 2023 |
| UK HE electricity cost | £0.28/kWh | HESA Estates Management Statistics 2022-23 |
| Heating season hours | 5,800 hrs/yr | CIBSE Guide A |
| Solar irradiance (Reading) | 950 kWh/m²/yr | PVGIS (EC JRC) |

## AI Agent Governance
- Agents may generate drafts only
- Humans must approve: architecture, financial models, emission calculations,
  external API integrations, security findings
- Agents must validate: imports, runtime, test coverage, security scan
- PRE_EXECUTION_PROMPT must be loaded at the start of every Claude Code session

## Release Principles
- No direct push to main
- Pull request required for all changes
- CI must pass 100% before merge
- Manual validation required at each phase checkpoint
- Financial outputs must be verified against known benchmarks before release

## Intellectual Property
- Copyright © 2026 Aparajita Parihar. All rights reserved.
- CrowAgent™ is an unregistered trademark (UK IPO Class 42 application pending)
- Greenfield University is a fictional institution for demonstration only
- Contact: crowagent.platform@gmail.com
