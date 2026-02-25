# ═══════════════════════════════════════════════════════════════════════════════
# CrowAgent™ Platform — Sustainability AI Decision Intelligence
# Target 1: Production-Grade MVP 
# ═══════════════════════════════════════════════════════════════════════════════

from __future__ import annotations
import base64
import os
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from dotenv import load_dotenv
_env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
load_dotenv(_env_path)

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import requests
from datetime import datetime, timezone

# ─────────────────────────────────────────────────────────────────────────────
# PATH SETUP
# ─────────────────────────────────────────────────────────────────────────────
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import services.weather as wx
import services.location as loc
import services.audit as audit
import core.agent as crow_agent
import core.physics as physics
from app.visualization_3d import render_campus_3d_map
from app.utils import validate_gemini_key
import app.compliance as compliance

# ─────────────────────────────────────────────────────────────────────────────
# ASSET LOADERS
# ─────────────────────────────────────────────────────────────────────────────
def _load_logo_uri() -> str:
    candidates = [
        os.path.join(os.path.dirname(__file__), "../assets/CrowAgent_Logo_Horizontal_Dark.svg"),
        os.path.join(os.getcwd(), "assets/CrowAgent_Logo_Horizontal_Dark.svg"),
    ]
    for path in candidates:
        if os.path.isfile(path):
            try:
                with open(path, "rb") as fh:
                    return f"data:image/svg+xml;base64,{base64.b64encode(fh.read()).decode()}"
            except Exception:
                pass
    return ""

def _load_icon_uri() -> str:
    candidates = [
        os.path.join(os.path.dirname(__file__), "../assets/CrowAgent_Icon_Square.svg"),
        os.path.join(os.getcwd(), "assets/CrowAgent_Icon_Square.svg"),
    ]
    for path in candidates:
        if os.path.isfile(path):
            try:
                with open(path, "rb") as fh:
                    return f"data:image/svg+xml;base64,{base64.b64encode(fh.read()).decode()}"
            except Exception:
                pass
    return ""

LOGO_URI = _load_logo_uri()
ICON_URI = _load_icon_uri()

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title   = "CrowAgent™ Platform",
    page_icon    = ICON_URI or "🌿",
    layout       = "wide",
    initial_sidebar_state = "expanded",
)

# [KEEP ALL YOUR EXISTING CSS STYLES HERE]
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;700&family=Nunito+Sans:ital,wght@0,300;0,400;0,600;0,700;1,400&display=swap');
html, body, [class*="css"] { font-family: 'Nunito Sans', sans-serif !important; }
h1,h2,h3,h4 { font-family: 'Rajdhani', sans-serif !important; letter-spacing: 0.3px; }
[data-testid="stAppViewContainer"] > .main { background: #F0F4F8; }
.block-container { padding-top: 0 !important; max-width: 100% !important; }
[data-testid="stSidebar"] { background: #071A2F !important; border-right: 1px solid #1A3A5C !important; }
[data-testid="stSidebar"] * { color: #CBD8E6 !important; }
.kpi-card { background: #ffffff; border-radius: 8px; padding: 18px 20px 14px; border: 1px solid #E0EBF4; border-top: 3px solid #00C2A8; box-shadow: 0 2px 8px rgba(7,26,47,.05); height: 100%; transition: transform 0.2s ease, box-shadow 0.2s ease; }
.kpi-card:hover { transform: translateY(-4px); box-shadow: 0 4px 12px rgba(7,26,47,.15); }
.kpi-label { font-family: 'Rajdhani', sans-serif; font-size: 0.78rem; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; color: #3A576B; margin-bottom: 6px; }
.kpi-value { font-family: 'Rajdhani', sans-serif; font-size: 2rem; font-weight: 700; color: #071A2F; line-height: 1.1; }
.kpi-unit { font-size: 0.9rem; font-weight: 500; color: #3A576B; margin-left: 2px; }
.sec-hdr { font-family: 'Rajdhani', sans-serif; font-size: 0.84rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #00C2A8; border-bottom: 1px solid rgba(0,194,168,.2); padding-bottom: 6px; margin-bottom: 14px; margin-top: 4px; }
.platform-topbar { background: linear-gradient(135deg, #071A2F 0%, #0D2640 60%, #0A2E40 100%); border-bottom: 2px solid #00C2A8; padding: 10px 24px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 16px; }
.chart-card { background: #ffffff; border-radius: 8px; border: 1px solid #E0EBF4; padding: 18px 18px 10px; box-shadow: 0 2px 8px rgba(7,26,47,.04); margin-bottom: 16px; }
.chart-title { font-family: 'Rajdhani', sans-serif; font-size: 0.88rem; font-weight: 700; letter-spacing: 0.5px; color: #071A2F; margin-bottom: 4px; text-transform: uppercase; }
.onboarding-card { background: #ffffff; border: 2px solid #E0EBF4; border-radius: 12px; padding: 30px; text-align: center; cursor: pointer; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
.onboarding-card:hover { border-color: #00C2A8; transform: translateY(-5px); box-shadow: 0 8px 25px rgba(0,194,168,0.15); }
#MainMenu { visibility: hidden; } footer { visibility: hidden; } header { background: transparent !important; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# INITIALISE STATE & REFRESH SURVIVAL (Phase 1)
# ─────────────────────────────────────────────────────────────────────────────
def _get_secret(key: str, default: str = "") -> str:
    try: return st.secrets[key]
    except Exception: return os.getenv(key, default)

# Check query params for F5 refresh survival
qp = st.query_params
if "segment" in qp:
    st.session_state.user_segment = qp["segment"]
    st.session_state.onboarded = True
elif "onboarded" not in st.session_state:
    st.session_state.onboarded = False

if "custom_buildings" not in st.session_state: st.session_state.custom_buildings = {}
if "chat_history" not in st.session_state: st.session_state.chat_history = []
if "agent_history" not in st.session_state: st.session_state.agent_history = []
if "gemini_key" not in st.session_state: st.session_state.gemini_key = _get_secret("GEMINI_KEY", "")
if "met_office_key" not in st.session_state: st.session_state.met_office_key = _get_secret("MET_OFFICE_KEY", "")
if "wx_city" not in st.session_state: st.session_state.wx_city = "Reading, Berkshire"
if "wx_lat" not in st.session_state: st.session_state.wx_lat = loc.CITIES["Reading, Berkshire"]["lat"]
if "wx_lon" not in st.session_state: st.session_state.wx_lon = loc.CITIES["Reading, Berkshire"]["lon"]
if "wx_location_name" not in st.session_state: st.session_state.wx_location_name = "Reading, Berkshire, UK"
if "wx_provider" not in st.session_state: st.session_state.wx_provider = "open_meteo"
if "manual_temp" not in st.session_state: st.session_state.manual_temp = 10.5

# ─────────────────────────────────────────────────────────────────────────────
# ONBOARDING GATE (Phase 1)
# ─────────────────────────────────────────────────────────────────────────────
if not st.session_state.onboarded:
    st.markdown("<div style='text-align:center; padding: 40px 0;'>", unsafe_allow_html=True)
    if LOGO_URI:
        st.markdown(f"<img src='{LOGO_URI}' width='300' style='margin-bottom:20px;'/>", unsafe_allow_html=True)
    st.markdown("<h1>Welcome to CrowAgent™ Platform</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#5A7A90; font-size:1.1rem; margin-bottom:40px;'>Select your profile to customize your AI dashboard and financial metrics.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,1,1])
    
    with col1:
        st.markdown("""<div class='onboarding-card'>
            <div style='font-size:3rem; margin-bottom:10px;'>🎓</div>
            <h3 style='color:#071A2F;'>University / School</h3>
            <p style='color:#5A7A90; font-size:0.9rem;'>Campus estate managers focusing on Net Zero targets and large-scale retrofits.</p>
        </div>""", unsafe_allow_html=True)
        if st.button("Select University", key="btn_uni", use_container_width=True):
            st.query_params["segment"] = "university_he"
            st.session_state.user_segment = "university_he"
            st.session_state.onboarded = True
            st.rerun()

    with col2:
        st.markdown("""<div class='onboarding-card'>
            <div style='font-size:3rem; margin-bottom:10px;'>🏢</div>
            <h3 style='color:#071A2F;'>SMB / Commercial Landlord</h3>
            <p style='color:#5A7A90; font-size:0.9rem;'>Property owners focusing on MEES compliance and EPC upgrades to avoid penalties.</p>
        </div>""", unsafe_allow_html=True)
        if st.button("Select Landlord", key="btn_smb", use_container_width=True):
            st.query_params["segment"] = "smb_landlord"
            st.session_state.user_segment = "smb_landlord"
            st.session_state.onboarded = True
            st.rerun()

    with col3:
        st.markdown("""<div class='onboarding-card'>
            <div style='font-size:3rem; margin-bottom:10px;'>🏭</div>
            <h3 style='color:#071A2F;'>SMB Industrial</h3>
            <p style='color:#5A7A90; font-size:0.9rem;'>Manufacturing and logistics focusing on SECR reporting and Scope 1 & 2 reductions.</p>
        </div>""", unsafe_allow_html=True)
        if st.button("Select Industrial", key="btn_ind", use_container_width=True):
            st.query_params["segment"] = "smb_industrial"
            st.session_state.user_segment = "smb_industrial"
            st.session_state.onboarded = True
            st.rerun()
            
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop() # Halt execution until a segment is chosen


# ─────────────────────────────────────────────────────────────────────────────
# BUILDING & SCENARIO DATA
# ─────────────────────────────────────────────────────────────────────────────
# Core physics dictionary import
BUILDINGS = physics.BUILDINGS
SCENARIOS = physics.SCENARIOS

# Merge Segment Defaults + Custom User Buildings
_seg_buildings = compliance.SEGMENT_BUILDINGS.get(st.session_state.user_segment, {})
_active_buildings = {**_seg_buildings, **BUILDINGS, **st.session_state.custom_buildings}

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    if LOGO_URI:
        st.markdown(f"<div style='padding:10px 0 4px; text-align:center;'><img src='{LOGO_URI}' width='200' alt='CrowAgent™ Logo'/></div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Show active segment with option to reset
    st.markdown("<div class='sb-section'>👤 Active Profile</div>", unsafe_allow_html=True)
    _smeta = compliance.SEGMENT_META[st.session_state.user_segment]
    st.markdown(f"<div style='color:#00C2A8; font-weight:bold;'>{_smeta['icon']} {_smeta['label']}</div>", unsafe_allow_html=True)
    if st.button("Switch Profile", size="small", use_container_width=True):
        st.query_params.clear()
        st.session_state.onboarded = False
        st.rerun()

    st.markdown("---")

    # ── Phase 2: Dynamic Portfolio Builder (No JSON) ─────────────────────────
    st.markdown("<div class='sb-section'>🏢 My Portfolio</div>", unsafe_allow_html=True)
    selected_building_name = st.selectbox("Select Building", list(_active_buildings.keys()), label_visibility="collapsed")
    
    with st.expander("➕ Add New Property", expanded=False):
        with st.form("add_property_form", clear_on_submit=True):
            st.markdown("<div style='font-size:0.8rem; color:#8FBCCE;'>Add up to 10 properties to your portfolio.</div>", unsafe_allow_html=True)
            p_name = st.text_input("Property Name", placeholder="e.g. High St Office")
            p_area = st.number_input("Floor Area (m²)", min_value=10, max_value=200000, value=500, step=50)
            p_age = st.selectbox("Built Era", ["Pre-1990 (Poor Insulation)", "1990-2010 (Average)", "Post-2010 (Modern)"])
            
            # Segment-specific form fields
            if st.session_state.user_segment == "smb_landlord":
                st.selectbox("Current EPC Rating (Optional)", ["E or lower", "D", "C", "B", "A"])
            elif st.session_state.user_segment == "smb_industrial":
                st.selectbox("Operation Type", ["Light Manufacturing", "Heavy Industrial", "Logistics/Warehouse"])
            
            p_submit = st.form_submit_button("Save Property", use_container_width=True)
            
            if p_submit and p_name:
                if len(st.session_state.custom_buildings) >= 10:
                    st.error("Portfolio limit reached (10 max).")
                else:
                    # Estimate physics metrics based on era
                    if p_age == "Pre-1990 (Poor Insulation)":
                        uw, ur, ug, eui = 2.1, 2.3, 3.1, 220
                    elif p_age == "1990-2010 (Average)":
                        uw, ur, ug, eui = 1.6, 1.8, 2.6, 140
                    else:
                        uw, ur, ug, eui = 0.8, 0.6, 1.6, 80
                        
                    st.session_state.custom_buildings[p_name] = {
                        "floor_area_m2": p_area,
                        "height_m": 4.0,
                        "glazing_ratio": 0.30,
                        "u_value_wall": uw,
                        "u_value_roof": ur,
                        "u_value_glazing": ug,
                        "baseline_energy_mwh": round((p_area * eui) / 1000, 1),
                        "occupancy_hours": 3000,
                        "description": f"Custom added property ({p_age})",
                        "built_year": p_age.split()[0],
                        "building_type": "Custom Property",
                        "segment": st.session_state.user_segment
                    }
                    st.rerun()

    st.markdown("---")

    # ── Scenarios: Auto-Defaulting (Phase 1/4) ───────────────────────────────
    st.markdown("<div class='sb-section'>🔧 Scenarios</div>", unsafe_allow_html=True)
    selected_scenario_names = st.multiselect(
        "Scenarios", 
        list(SCENARIOS.keys()),
        default=["Baseline (No Intervention)", "Combined Package (All Interventions)"], # Default to maximum ROI
        label_visibility="collapsed",
    )

    if not selected_scenario_names:
        st.warning("⚠ Select at least one scenario to continue.")
        st.stop()

    st.markdown("---")
    
    # Weather and Location logic remains identical to preserve your backend logic
    st.markdown("<div class='sb-section'>📍 Location & Live Weather</div>", unsafe_allow_html=True)
    _city_list = loc.city_options()
    _city_idx  = _city_list.index(st.session_state.wx_city) if st.session_state.wx_city in _city_list else 0
    _sel_city  = st.selectbox("City / Region", _city_list, index=_city_idx, label_visibility="collapsed")
    if _sel_city != st.session_state.wx_city:
        _meta = loc.city_meta(_sel_city)
        st.session_state.wx_city = _sel_city
        st.session_state.wx_lat, st.session_state.wx_lon = _meta["lat"], _meta["lon"]
        st.session_state.wx_location_name = f"{_sel_city}, {_meta['country']}"
        st.rerun()

    with st.spinner("Fetching weather..."):
        weather = wx.get_weather(lat=st.session_state.wx_lat, lon=st.session_state.wx_lon, location_name=st.session_state.wx_location_name)
    
    st.markdown(f"""<div style='background:#0D2640; border-radius:8px; padding:12px; margin-top:10px;'>
        <div style='font-size:1.6rem; color:#fff;'>{weather['condition_icon']} {weather['temperature_c']}°C</div>
        <div style='font-size:0.8rem; color:#A8C8D8;'>{weather['condition']} in {weather['location_name']}</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("---")
    
    # API Keys Expander
    with st.expander("🔑 API Keys (AI Advisor)"):
        _gm_key = st.text_input("Gemini API Key", type="password", value=st.session_state.gemini_key)
        if _gm_key != st.session_state.gemini_key:
            st.session_state.gemini_key = _gm_key
            st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# COMPUTE PHYSICS ENGINE
# ─────────────────────────────────────────────────────────────────────────────
results = {}
sb = _active_buildings[selected_building_name]
for _sn in selected_scenario_names:
    try:
        results[_sn] = physics.calculate_thermal_load(sb, SCENARIOS[_sn], weather)
    except Exception as _e:
        st.sidebar.error(f"Error computing {_sn}: {_e}")

baseline_result = results.get("Baseline (No Intervention)", list(results.values())[0] if results else {})

# ─────────────────────────────────────────────────────────────────────────────
# TOP HEADER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class='platform-topbar'>
  <div style='display:flex;align-items:center;gap:16px;'>
    <span style='font-family:Rajdhani,sans-serif;font-size:1.4rem;font-weight:700;color:#00C2A8;'>CrowAgent™</span>
    <span style='color:#8FBCCE; font-size:0.9rem; margin-top:2px;'>Enterprise Sustainability Intelligence</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# MAIN TABS & SEGMENT-RESPONSIVE DASHBOARD (Phase 4)
# ─────────────────────────────────────────────────────────────────────────────
_tab_dash, _tab_fin, _tab_ai, _tab_map = st.tabs([
    "📊 Executive Dashboard",
    "📈 Financial & Compliance ROI",
    "🤖 AI Sustainability Advisor",
    "🗺️ Interactive 3D Map",
])

# Determine dynamic wording based on Segment
if st.session_state.user_segment == "smb_landlord":
    kpi_title_2 = "MEES Penalty Avoidance"
    kpi_title_3 = "EPC Rating Uplift"
elif st.session_state.user_segment == "smb_industrial":
    kpi_title_2 = "Scope 1 & 2 Reductions"
    kpi_title_3 = "SECR Intensity Drop"
else:
    kpi_title_2 = "Best Energy Saving"
    kpi_title_3 = "Best Carbon Reduction"

with _tab_dash:
    st.markdown(f"<h2>{selected_building_name}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#5A7A90;'>{sb['description']} | Built: {sb['built_year']} | {sb['floor_area_m2']:,} m²</p>", unsafe_allow_html=True)

    if results:
        best_saving = max(results.values(), key=lambda r: r.get("energy_saving_pct", 0))
        best_carbon = max(results.values(), key=lambda r: r.get("carbon_saving_t", 0))
        baseline_energy = baseline_result.get("baseline_energy_mwh", sb["baseline_energy_mwh"])
        baseline_co2 = round(baseline_energy * 1000 * 0.20482 / 1000, 1)

        k1, k2, k3, k4 = st.columns(4)
        with k1:
            st.markdown(f"<div class='kpi-card'><div class='kpi-label'>Current Baseline</div><div class='kpi-value'>{baseline_energy:,.0f}<span class='kpi-unit'>MWh/yr</span></div></div>", unsafe_allow_html=True)
        with k2:
            st.markdown(f"<div class='kpi-card accent-green'><div class='kpi-label'>{kpi_title_2}</div><div class='kpi-value'>{best_saving.get('energy_saving_pct',0)}<span class='kpi-unit'>%</span></div></div>", unsafe_allow_html=True)
        with k3:
            st.markdown(f"<div class='kpi-card' style='border-top-color:#00C2A8'><div class='kpi-label'>{kpi_title_3}</div><div class='kpi-value'>{best_carbon.get('carbon_saving_t',0):,.0f}<span class='kpi-unit'>t CO₂e</span></div></div>", unsafe_allow_html=True)
        with k4:
            st.markdown(f"<div class='kpi-card accent-gold'><div class='kpi-label'>Baseline Cost</div><div class='kpi-value'>£{round(baseline_energy * 280, 1):,.0f}</div></div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='chart-card'><div class='chart-title'>⚡ Energy Consumption (MWh)</div>", unsafe_allow_html=True)
        fig_e = go.Figure()
        for sn, res in results.items():
            fig_e.add_trace(go.Bar(x=[sn.split("(")[0]], y=[res["scenario_energy_mwh"]], marker_color=SCENARIOS[sn]["colour"], name=sn))
        fig_e.update_layout(height=300, plot_bgcolor="rgba(0,0,0,0)", showlegend=False)
        st.plotly_chart(fig_e, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='chart-card'><div class='chart-title'>🌍 Carbon Emissions (t CO₂e)</div>", unsafe_allow_html=True)
        fig_c = go.Figure()
        for sn, res in results.items():
            fig_c.add_trace(go.Bar(x=[sn.split("(")[0]], y=[res["scenario_carbon_t"]], marker_color=SCENARIOS[sn]["colour"], name=sn))
        fig_c.update_layout(height=300, plot_bgcolor="rgba(0,0,0,0)", showlegend=False)
        st.plotly_chart(fig_c, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

with _tab_fin:
    paid_scenarios = {n: r for n, r in results.items() if SCENARIOS[n]["install_cost_gbp"] > 0}
    if not paid_scenarios:
        st.info("Select an intervention scenario (like Combined Package) to view financial ROI.")
    else:
        # Segment specific financial headers
        if st.session_state.user_segment == "smb_landlord":
            st.error("🚨 **MEES 2028 Warning:** Properties rated below EPC C will be unlettable. The investments below represent necessary capital expenditure to avoid severe civil penalties.")
        
        st.markdown("<div class='sec-hdr'>10-Year Cumulative Net Cash Flow</div>", unsafe_allow_html=True)
        fig_ncf = go.Figure()
        years = list(range(0, 11))
        for sn, res in paid_scenarios.items():
            cashflow = [-res["install_cost_gbp"] + res["annual_saving_gbp"] * y for y in years]
            fig_ncf.add_trace(go.Scatter(x=years, y=cashflow, name=sn.split("(")[0], line=dict(color=SCENARIOS[sn]["colour"], width=3)))
        fig_ncf.add_hline(y=0, line=dict(dash="dot", color="#C0C8D0"))
        fig_ncf.update_layout(height=350, plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_ncf, use_container_width=True)

with _tab_ai:
    _akey = st.session_state.gemini_key
    if not _akey:
        st.warning("🔑 Please enter your Gemini API Key in the sidebar to activate the AI Advisor.")
    else:
        st.markdown("### 🤖 Ask the Physics-Informed AI")
        for _msg in st.session_state.chat_history:
            role_icon = "👤 You" if _msg["role"] == "user" else "🤖 AI"
            st.markdown(f"**{role_icon}:** {_msg['content']}")
            
        with st.form("ai_chat", clear_on_submit=True):
            user_input = st.text_input("Ask a question about your portfolio...", placeholder="Which building saves the most carbon?")
            if st.form_submit_button("Send") and user_input:
                st.session_state.chat_history.append({"role": "user", "content": user_input})
                with st.spinner("Running simulations..."):
                    res = crow_agent.run_agent(_akey, user_input, st.session_state.agent_history, _active_buildings, SCENARIOS, physics.calculate_thermal_load)
                    st.session_state.chat_history.append({"role": "model", "content": res.get("answer", "Error computing answer.")})
                st.rerun()

with _tab_map:
    # Phase 3 mapping execution utilizing PyDeck and Geo-location
    st.markdown("""
    <div style='background:#E0EBF4; padding:15px; border-radius:8px; margin-bottom:15px;'>
    <strong>🗺️ Map Note:</strong> Using your Postcode search below will immediately re-center the PyDeck Digital Twin. 
    You can click the 3D polygons overlaid on the map to inspect their real-time physics data.
    </div>
    """, unsafe_allow_html=True)
    render_campus_3d_map(selected_scenario_names, weather)