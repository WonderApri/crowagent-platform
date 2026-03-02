# PRE-EXECUTION AGENT DIRECTIVE
**Load this file at the start of every Claude Code session.**

---

You are operating within the CrowAgent™ governed repository.

## STRICT RULES — NO EXCEPTIONS

1. Do NOT hallucinate files, functions, or constants
2. Do NOT modify thermal model, financial formulas, or emission factors
   unless REQUIREMENTS_SPEC.md explicitly authorises it
3. Do NOT introduce new Python dependencies without asking first
4. Do NOT alter the architecture pattern (app/core/services/config separation)
5. Do NOT change API signatures or function contracts
6. Do NOT change session_state keys without approval
7. Do NOT hardcode secrets — always use .streamlit/secrets.toml or .env
8. Preserve backward compatibility at all times

## BEFORE MAKING ANY CHANGE

- Read the full file you are about to modify
- Map its imports and dependencies
- Identify all callers of functions you will change
- Confirm the change is within your current phase scope

## AFTER EVERY CHANGE

Validate:
- [ ] No ImportError on startup
- [ ] No NameError or AttributeError
- [ ] `streamlit run app/main.py` runs without crash
- [ ] Financial values match REQUIREMENTS_SPEC.md
- [ ] Emission totals unchanged
- [ ] Portfolio session state persists across tab switches
- [ ] Map renders without error

## OUTPUT FORMAT FOR EVERY TASK

Provide:
1. List of files modified
2. Summary of what changed and why
3. Any assumptions made (flag for human review)
4. Validation confirmation
5. Any concerns or questions for the human reviewer

## NEVER AUTO-PROCEED PAST A CHECKPOINT

When you reach a human checkpoint, stop and output:
```
⏸ HUMAN CHECKPOINT [N] REACHED
Please review the above output and confirm before I proceed.
```
