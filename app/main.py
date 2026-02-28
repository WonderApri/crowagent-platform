"""
Main application logic for the Streamlit app.
"""
import streamlit as st
import importlib
from app.session import initialize_session_state
from app.branding import display_branding
from app.utils import show_congratulations
from config.constants import SEGMENT_DEFINITIONS

def get_segment_class(segment_name):
    """
    Dynamically imports and returns the class for a given segment.
    """
    segment_info = SEGMENT_DEFINITIONS.get(segment_name)
    if not segment_info:
        return None
    
    module_name = segment_info["module"]
    class_name = segment_info["class"]
    
    try:
        module = importlib.import_module(module_name)
        segment_class = getattr(module, class_name)
        return segment_class
    except (ImportError, AttributeError) as e:
        st.error(f"Error loading segment '{segment_name}': {e}")
        return None

def run():
    """
    The main function that orchestrates the Streamlit application.
    """
    st.set_page_config(
        page_title="CrowAgent Insights",
        page_icon=":bird:",
        layout="wide"
    )

    initialize_session_state()
    display_branding()

    st.sidebar.title("Segment Selection")
    
    # Segment selection dropdown
    segment_options = list(SEGMENT_DEFINITIONS.keys())
    selected_segment_name = st.sidebar.selectbox(
        "Choose your customer segment:",
        options=[""] + segment_options,  # Add an empty option
        index=0,
        key="segment_selector"
    )

    # Instantiate the selected segment
    if selected_segment_name and st.session_state.get('segment_name') != selected_segment_name:
        SegmentClass = get_segment_class(selected_segment_name)
        if SegmentClass:
            st.session_state['segment'] = SegmentClass()
            st.session_state['segment_name'] = selected_segment_name
    elif not selected_segment_name:
        st.session_state['segment'] = None
        st.session_state['segment_name'] = "No segment selected"

    # Main panel rendering
    if st.session_state.get('segment'):
        st.session_state['segment'].render()
    else:
        st.title("Welcome to CrowAgent")
        st.write("Please select a customer segment from the sidebar to begin.")

    # A button to demonstrate a utility function
    if st.button("Show Congratulations"):
        show_congratulations()
