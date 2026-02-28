"""
Manages session state for the Streamlit application.
"""
import streamlit as st

def initialize_session_state():
    """Initializes the session state with default values."""
    if 'segment' not in st.session_state:
        st.session_state['segment'] = None
    if 'segment_name' not in st.session_state:
        st.session_state['segment_name'] = "No segment selected"
