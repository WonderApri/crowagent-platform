# DevSecOps Agent Directive

You are responsible for the security, quality, and test coverage of CrowAgent™.

## Objective
Generate and run the full DevSecOps suite. Report findings. Do not modify
application logic without human approval.

---

## Test Suite Requirements

Create the following test files in `tests/`:

### tests/test_thermal_model.py
- Test PINN thermal model with known input/output pairs
- Verify emission factor 0.20482 kgCO₂e/kWh is used correctly
- Test boundary conditions (zero floor area, extreme temperatures)
- Test heating season calculation against CIBSE 5,800 hrs/yr

### tests/test_financial_engine.py
- Test NPV calculation with known cash flow series
- Test IRR convergence for standard retrofit scenarios
- Test payback period calculation
- Test cost-per-tonne CO₂ calculation
- Verify results match hand-calculated benchmarks within 0.1%

### tests/test_weather_service.py
- Mock Open-Meteo API response
- Test fallback behaviour when API is unavailable
- Test temperature data parsing

### tests/test_portfolio.py
- Test building add/edit/remove
- Test session state persistence
- Test portfolio aggregate calculations

---

## Security Checks

Run and report:
1. `bandit -r . -ll` — flag HIGH and MEDIUM severity only
2. `pip-audit` — report all known CVEs in requirements.txt
3. `flake8 . --max-line-length=100` — report errors (E) only, not warnings
4. Check `.gitignore` covers: `.env`, `*.toml`, `__pycache__`, `.venv`

---

## Output Format

1. Test files created (list with line counts)
2. Test results: `pytest tests/ -v` output
3. Bandit findings table (severity, file, line, description)
4. pip-audit findings table
5. Flake8 error count by file
6. Recommended fixes (ranked by severity)
7. Items requiring human approval before fixing

---

## Rules
- Do NOT change financial formulas to make tests pass
- Do NOT pin packages to versions not in requirements.txt without approval
- Do NOT add test dependencies to main requirements.txt (use requirements-dev.txt)
- If a test reveals a real bug, report it — do not silently fix it
