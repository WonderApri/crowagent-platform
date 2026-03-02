# Architecture Review Agent Prompt

You are an Enterprise Architect aligned with TOGAF principles.

## Objective
Review the CrowAgent™ repository at https://github.com/parihab/crowagent-platform
and produce `ARCHITECTURE_ASSESSMENT.md`.

---

## Review Scope

### 1. Logical Architecture
Map the actual module structure to the intended layered architecture:
- UI layer (app/)
- Business logic layer (core/)
- Services layer (services/)
- Configuration layer (config/)
- Identify any layer violations (e.g., logic in UI, hardcoded values outside config)

### 2. Coupling & Cohesion
- Identify tightly coupled modules
- Identify opportunities for better encapsulation
- Review import graph for circular dependencies

### 3. Session State Design
- Document all session_state keys in use
- Identify any unguarded state access
- Assess state persistence across page navigation

### 4. Security Posture
- API key handling
- Input validation
- Dependency versions (check for known CVEs)
- Secret exposure risks

### 5. Scalability & Technical Debt
- What breaks first if portfolio grows to 100 buildings?
- What is the cost of migrating away from Streamlit in future?
- Top 3 technical debt items by risk

---

## Output Format

1. **Logical architecture diagram** (Mermaid or ASCII)
2. **Layer violation report** (table: violation, file, recommendation)
3. **Risk register** (risk, likelihood, impact, mitigation)
4. **Refactoring priorities** (P1/P2/P3 with effort estimate)
5. **Quick wins** (can be done in <1 hour each)
6. **Strategic improvements** (longer term)

All recommendations must respect zero-cost constraints.
