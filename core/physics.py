# © 2026 Aparajita Parihar. All rights reserved.
# CrowAgent™ Platform — Core Physics Engine
# PINN Thermal Model Logic
 
import numpy as np
 
# ── BUILDING DATA ─────────────────────────────────────────────────────────────
# Derived from HESA 2022-23 UK HE sector averages
BUILDINGS = {
    "Greenfield Library": {
        "floor_area_m2": 8500, "height_m": 4.5, "glazing_ratio": 0.35,
        "u_value_wall": 1.8, "u_value_roof": 2.1, "u_value_glazing": 2.8,
        "baseline_energy_mwh": 487, "occupancy_hours": 3500,
        "building_type": "Library / Learning Hub", "built_year": "Pre-1990",
        "description": "Main campus library — 8,500 m² · 5 floors · Heavy glazing"
    },
    "Greenfield Arts Building": {
        "floor_area_m2": 11200, "height_m": 5.0, "glazing_ratio": 0.28,
        "u_value_wall": 2.1, "u_value_roof": 1.9, "u_value_glazing": 3.1,
        "baseline_energy_mwh": 623, "occupancy_hours": 4000,
        "building_type": "Teaching / Lecture", "built_year": "Pre-1985",
        "description": "Humanities faculty — 11,200 m² · 6 floors · Lecture theatres"
    },
    "Greenfield Science Block": {
        "floor_area_m2": 6800, "height_m": 4.0, "glazing_ratio": 0.30,
        "u_value_wall": 1.6, "u_value_roof": 1.7, "u_value_glazing": 2.6,
        "baseline_energy_mwh": 391, "occupancy_hours": 3200,
        "building_type": "Laboratory / Research", "built_year": "Pre-1995",
        "description": "Science laboratories — 6,800 m² · 4 floors · Lab-heavy usage"
    }
}
 
SCENARIOS = {
    "Baseline (No Intervention)": {
        "u_wall_factor": 1.0, "u_roof_factor": 1.0, "u_glazing_factor": 1.0,
        "solar_gain_reduction": 0.0, "infiltration_reduction": 0.0,
        "renewable_kwh": 0, "install_cost_gbp": 0, "colour": "#4A6FA5", "icon": "🏢"
    },
    "Solar Glass Installation": {
        "u_wall_factor": 1.0, "u_roof_factor": 1.0, "u_glazing_factor": 0.55,
        "solar_gain_reduction": 0.15, "infiltration_reduction": 0.05,
        "renewable_kwh": 42000, "install_cost_gbp": 280000, "colour": "#00C2A8", "icon": "☀️"
    },
    # ... (Include other scenarios from your original app.py here)
}
 
def calculate_thermal_load(building, scenario, weather_data):
    """
    Physics-informed thermal load calculation based on Raissi et al. (2019).
    """
    b, s, temp = building, scenario, weather_data["temperature_c"]
    
    # Geometry & Thermal Calculations
    perimeter_m = 4.0 * (b["floor_area_m2"] ** 0.5)
    wall_area_m2 = perimeter_m * b["height_m"] * (1.0 - b["glazing_ratio"])
    glazing_area_m2 = perimeter_m * b["height_m"] * b["glazing_ratio"]
    roof_area_m2 = b["floor_area_m2"]
    volume_m3 = b["floor_area_m2"] * b["height_m"]
 
    u_wall, u_roof, u_glazing = b["u_value_wall"]*s["u_wall_factor"], b["u_value_roof"]*s["u_roof_factor"], b["u_value_glazing"]*s["u_glazing_factor"]
    
    delta_t, heating_hrs = max(0.0, 21.0 - temp), 5800.0
    q_trans_mwh = (u_wall*wall_area_m2 + u_roof*roof_area_m2 + u_glazing*glazing_area_m2) * delta_t * heating_hrs / 1_000_000.0
    
    # Final metrics calculation (Carbon, Energy, Financials)
    # ... (Keep the rest of your math logic here)
    return { "energy_saving_mwh": 10.5, "carbon_saving_t": 2.1, "u_wall": u_wall, "u_roof": u_roof, "u_glazing": u_glazing } # Placeholder for brevity