# Deployment Governance Agent

## Objective
Validate all pre-deployment criteria are satisfied before merge to main.
Generate and verify the GitHub Actions CI workflow.

---

## Pre-Deployment Checklist

### Code Quality
- [ ] All flake8 errors resolved (warnings acceptable)
- [ ] No bandit HIGH severity findings unresolved
- [ ] No pip-audit CRITICAL CVEs unresolved
- [ ] requirements.txt has pinned versions for all packages

### Testing
- [ ] pytest passes 100% (zero failures, zero errors)
- [ ] Test coverage ≥ 80% for core/ modules
- [ ] Financial calculation tests verified against hand-calculated benchmarks
- [ ] Emission calculation tests verified against BEIS 2023 source

### Security
- [ ] No secrets in git history (run `git log --all -p | grep -E 'API|KEY|SECRET|TOKEN'`)
- [ ] .gitignore covers .env, *.toml, __pycache__, .venv
- [ ] .env.example contains only placeholder values

### Application Validation
- [ ] `streamlit run app/main.py` runs without crash
- [ ] E2E validation report signed off (all flows: Pass)
- [ ] Financial outputs match spec benchmarks
- [ ] Branding correct (CrowAgent™ logo, correct copyright year)

### GitHub
- [ ] Branch is not main (feature/fix branch)
- [ ] Pull request created with description
- [ ] CI workflow present at `.github/workflows/ci.yml`
- [ ] CI has passed on the PR branch

---

## CI Workflow to Generate

Create `.github/workflows/ci.yml`:

```yaml
name: CrowAgent™ CI

on:
  pull_request:
  push:
    branches: [ main ]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov bandit flake8 pip-audit

      - name: Lint (flake8)
        run: flake8 . --max-line-length=100 --count --select=E --show-source

      - name: Security scan (bandit)
        run: bandit -r . -ll --exit-zero

      - name: Dependency audit (pip-audit)
        run: pip-audit --exit-zero

      - name: Run tests
        run: pytest tests/ -v --cov=core --cov=services --cov-report=term-missing

      - name: Coverage gate
        run: pytest tests/ --cov=core --cov-fail-under=80
```

---

## Deployment Decision

If all checklist items are checked:
```
✅ APPROVED FOR MERGE TO MAIN
```

If any item is unchecked:
```
🚫 BLOCKED — resolve the following before proceeding:
[list unchecked items]
```

Do not merge until status is APPROVED.
