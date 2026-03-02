# Requirements Specification Agent Prompt

You are a Chartered Sustainability & Financial Systems Architect.

## Objective
Produce a deterministic, complete requirements specification for CrowAgent™ Platform.
Output as `REQUIREMENTS_SPEC.md`. No implementation. Specification only.

---

## Required Sections

### 1. Functional Requirements
- FR1: Portfolio ingestion — add, edit, remove buildings with attributes
  (floor area, building type, age, current U-values, current energy use)
- FR2: Scenario modelling — define and compare retrofit interventions
  (e.g., wall insulation, roof insulation, glazing upgrade, ASHP, PV)
- FR3: Financial metrics — NPV, IRR, payback period, ROI, cost-per-tonne CO₂
  per building and per portfolio aggregate
- FR4: Emission calculation — annual kgCO₂e using BEIS 2023 factors
- FR5: Compliance evaluation — against Net Zero pathway thresholds
- FR6: AI advisory — Gemini 1.5 Flash with physics tool-use for recommendations
- FR7: Weather integration — live temperature from Open-Meteo for thermal model
- FR8: Dashboard — KPI summary across all buildings and scenarios

### 2. Non-Functional Requirements
- NFR1: Financial accuracy — all outputs must match hand-calculated benchmarks
  to within 0.1%
- NFR2: Performance — UI response <2s for portfolio of up to 20 buildings
- NFR3: Security — no secrets in code or git history; session-only API key storage
- NFR4: Determinism — same inputs must always produce same outputs
- NFR5: Portability — runs on Python 3.11 with zero paid services required

### 3. Data Contracts
Define schemas for:
- Asset model (building attributes)
- Scenario model (intervention parameters)
- Financial output model
- Emission output model
- Weather data model

### 4. Constraints
- Streamlit UI only — no React, Vue, or other frameworks
- Zero paid external services (Gemini free tier acceptable)
- GitHub-hosted, GitHub Actions CI
- Must run locally without internet (except AI Advisor feature)

### 5. Acceptance Criteria
For each functional requirement, define a measurable pass/fail test condition.

---

## Output Instructions
- Use clear numbered headings
- Include a data schema for each model (Python TypedDict or dataclass format)
- Flag any requirement that cannot be met without clarification
- Do not include implementation code
