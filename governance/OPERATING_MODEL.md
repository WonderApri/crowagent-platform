# CrowAgent™ — AI-Augmented SDLC Operating Model

This document defines the 3-team governance structure used to build and maintain
CrowAgent™ Platform with Claude Code as the agentic development engine.

---

## Operating Principle

Claude Code generates. Humans approve. No exceptions for financial logic,
physics models, or security controls.

---

## Team 1 — Requirements & Architecture (SpecOps)

**Owns:** Platform spec · Architecture blueprint · Data contracts · NFRs
**AI role:** Claude Code drafts → Human reviews → Claude Code refines
**Deliverables:**
- `REQUIREMENTS_SPEC.md`
- `ARCHITECTURE_ASSESSMENT.md`
- Data schema definitions

**Key prompts:** `02_SPECIFICATION_AGENT.md`, `03_ARCHITECTURE_REVIEW_AGENT.md`

**Checkpoint:** Architecture must be approved in writing before Team 2 begins.

---

## Team 2 — DevSecOps

**Owns:** Application code · Infra config · Security controls · Test suite
**AI role:** Claude Code builds → Human reviews → Claude Code fixes
**Deliverables:**
- All modules in `app/`, `core/`, `services/`, `config/`
- `tests/` suite with >80% coverage
- Security scan reports (bandit, pip-audit)
- Lint compliance (flake8)

**Key prompts:** `00_PRE_EXECUTION_PROMPT.md`, `04_DEVSECOPS_AGENT.md`

**Checkpoint:** All tests must pass and security findings must be reviewed
before Team 3 begins.

---

## Team 3 — QA & Deployment Governance

**Owns:** E2E validation · Release approval · GitHub pipeline enforcement
**AI role:** Claude Code validates → Human signs off → Human deploys
**Deliverables:**
- E2E validation report
- CI/CD pipeline (`.github/workflows/ci.yml`)
- Signed-off release notes

**Key prompts:** `05_E2E_VALIDATION_AGENT.md`, `06_DEPLOYMENT_GOVERNANCE.md`

**Checkpoint:** All 7 BCP phases must be signed off before merge to main.

---

## Human-in-Loop Checkpoints Summary

| Checkpoint | Gate | Owner |
|-----------|------|-------|
| 0 | Environment confirmed running | Team 1 |
| 1 | Context summary reviewed | Team 1 |
| 2 | Requirements spec approved | Team 1 |
| 3 | Architecture approved | Team 1 |
| 4 | Platform runs + financial outputs verified | Team 2 |
| 5 | Security + test results reviewed | Team 2 |
| 6 | E2E validation signed off | Team 3 |
| 7 | CI green + merge approved | Team 3 |

---

## Why This Model Works

Traditional SDLC risk: AI generates confident but wrong code.
This model's answer: Every phase has a human gate. Claude Code cannot proceed
past a checkpoint without explicit human approval. The prompt files enforce
this by requiring the human to acknowledge results before the next phase prompt
is issued.

The result is an SDLC that is ~85% faster than manual development while
maintaining the accuracy and governance standards of enterprise software.
