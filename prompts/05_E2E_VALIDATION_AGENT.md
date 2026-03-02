# End-to-End Validation Agent

## Objective
Simulate the complete CrowAgent™ user flow and produce a validation report.
Do not auto-fix any failures — report them for human review.

---

## User Flow to Simulate

### Flow 1: New User — First Run
1. Launch `streamlit run app/main.py`
2. Confirm homepage loads with CrowAgent™ logo and branding
3. Confirm demo portfolio is pre-loaded (Greenfield University buildings)
4. Navigate to Dashboard tab — verify KPI cards render
5. Navigate to Financial Analysis tab — verify tables and charts render
6. Navigate to AI Advisor tab — verify prompt input is present

### Flow 2: Portfolio Management
1. Add a new building via the "➕ Add building" control
2. Confirm building appears in portfolio
3. Add a new scenario via "➕ Add scenario"
4. Confirm scenario appears in scenario list
5. Switch between buildings — confirm state persists
6. Navigate away and back — confirm portfolio still intact

### Flow 3: Financial Calculations
1. Set discount rate to 5%
2. Set project life to 25 years
3. Select a retrofit scenario
4. Record: NPV, IRR, payback period, cost-per-tonne CO₂
5. Change discount rate to 8%
6. Verify NPV changes correctly (should decrease for positive cash flows)
7. Verify IRR is unchanged (independent of discount rate)

### Flow 4: AI Advisor (requires Gemini API key)
1. Enter a valid Gemini API key
2. Submit a query about wall insulation for a demo building
3. Confirm a structured response is returned
4. Confirm no raw API errors appear in the UI

### Flow 5: Weather Integration
1. Confirm live temperature is displayed on dashboard
2. If Open-Meteo is unavailable, confirm graceful fallback (no crash)

---

## Validation Checklist

For each flow, report:
- [ ] No runtime errors or tracebacks
- [ ] No Streamlit warning messages in terminal
- [ ] Financial outputs are deterministic (same inputs = same outputs)
- [ ] Portfolio state persists across tab navigation
- [ ] Session state keys match documented list in CONTEXT.md
- [ ] No hardcoded secrets visible in UI or source
- [ ] Logo renders (not emoji fallback)
- [ ] Map renders if map feature is active

---

## Output Format

1. Flow-by-flow results (Pass/Fail/Partial with notes)
2. Full list of failures with file, line, and description
3. Regression risks (things that work but feel fragile)
4. Sign-off recommendation: READY FOR DEPLOYMENT / BLOCKED
