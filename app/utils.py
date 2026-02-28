"""
Utility functions for the Streamlit application.
"""
import streamlit as st
import time

def show_congratulations():
    """Displays a congratulations message and balloons."""
    st.success("Congratulations! You've successfully run the script.")
    time.sleep(1)
    st.balloons()
