"""
Handles the branding and sidebar elements of the application.
"""
import streamlit as st
from config.constants import CROWAGENT_LOGO_HORIZONTAL_DARK_URL

def display_branding():
    """
    Displays the CrowAgent logo and the 'About' section in the sidebar.
    """
    st.sidebar.image(CROWAGENT_LOGO_HORIZONTAL_DARK_URL, use_column_width=True)
    st.sidebar.markdown("---")
    st.sidebar.info(
        "**About CrowAgent**\n\n"
        "This tool is a prototype from the R&D department. "
        "Use with caution and report any bugs."
    )
