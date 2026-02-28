import streamlit as st
from app.segments import SEGMENT_LABELS

def render_sidebar():
    """
    Renders the sidebar and returns (segment_id, weather_dict, location_name).
    If no segment is selected, renders the onboarding gate and returns (None, None, None).
    """
    # Onboarding Gate
    if not st.session_state.get("user_segment"):
        st.title("Welcome to CrowAgent™")
        st.markdown("### Select your segment to begin:")
        
        cols = st.columns(2)
        for i, (seg_id, label) in enumerate(SEGMENT_LABELS.items()):
            with cols[i % 2]:
                if st.button(label, key=f"btn_{seg_id}", use_container_width=True):
                    st.session_state.user_segment = seg_id
                    st.rerun()
        return None, None, None

    # Normal Sidebar
    with st.sidebar:
        st.header("CrowAgent™")
        st.caption(f"Segment: {SEGMENT_LABELS.get(st.session_state.user_segment)}")
        
        if st.button("Change Segment"):
            st.session_state.user_segment = None
            st.rerun()
            
        st.divider()
        st.subheader("📍 Location")
        st.text("Reading, UK (Default)")
        
        # Placeholder weather return
        weather = {"temperature_c": 12.5, "condition": "Cloudy"}
        
        return st.session_state.user_segment, weather, "Reading, UK"