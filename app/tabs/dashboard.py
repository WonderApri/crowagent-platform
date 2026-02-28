import streamlit as st

def render(handler, weather, portfolio):
    st.subheader(f"{handler.display_label} Dashboard")
    
    # Import _card from main to avoid circular import at module level
    from app.main import _card
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: _card("Energy Saved", "0 MWh", "vs Baseline")
    with col2: _card("Carbon Saved", "0 tCO2", "vs Baseline")
    with col3: _card("Cost Saved", "£0", "Annual")
    with col4: _card("Payback", "N/A", "Years")
    
    st.info("Add buildings to your portfolio to see analysis.")