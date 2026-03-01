import streamlit as st
import os

MAX_CHAT_HISTORY = 40

def _get_secret(key: str, default: str = "") -> str:
    """
    Retrieve a secret from Streamlit secrets or environment variables.
    """
    try:
        if hasattr(st, "secrets") and key in st.secrets:
            return st.secrets[key]
    except Exception:
        pass
    return os.getenv(key, default)

def init_session():
    """
    Initialise all session state keys with defaults.
    Idempotent.
    """
    defaults = {
        "user_segment": None,
        "portfolio": [],
        "active_analysis_ids": [],
        "chat_history": [],
        "agent_history": [],
        "gemini_key": "",
        "gemini_key_valid": False,
        "energy_tariff_gbp_per_kwh": 0.28,
        "weather_provider": "open_meteo",
        "building_names": {},
        "selected_scenario_names": [],
        "onboarding_complete": False,
    }

    for key, value in defaults.items():
        st.session_state.setdefault(key, value)