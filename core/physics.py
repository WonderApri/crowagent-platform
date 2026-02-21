<<<<<<< HEAD
# ══════════════════════════════════════════════════════════════════════════════
# CrowAgent™ Platform — Physics-Informed Thermal Model
# © 2026 Aparajita Parihar. All rights reserved.
#
# PINN-inspired simplified physics model for campus building thermal load estimation
# Includes interventions such as: solar glass, green roofs, enhanced insulation, renewables
# ══════════════════════════════════════════════════════════════════════════════

from typing import Dict, Any

# ─────────────────────────────────────────────────────────────────────────────
# PHYSICS CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────
CARBON_INTENSITY_KG_CO2_PER_KWH = 0.20482  # BEIS 2023 UK grid mix
ELECTRICITY_COST_GBP_PER_KWH = 0.28  # HESA 2022-23 HE sector average
HEATING_SETPOINT_C = 21  # UK Building Regulations Part L
HEATING_SEASON_HOURS_PER_YEAR = 5800  # CIBSE Guide A
SOLAR_IRRADIANCE_KWH_M2_PER_YEAR = 950  # PVGIS Reading, UK

# ─────────────────────────────────────────────────────────────────────────────
# BUILDING DATABASE
# Based on published UK HE sector averages — fictional buildings for demonstration
# ─────────────────────────────────────────────────────────────────────────────
BUILDINGS: Dict[str, Dict[str, Any]] = {
    "Greenfield Library": {
        "u_value_wall": 0.35,              # W/m²K — current performance
        "u_value_roof": 0.25,
        "u_value_window": 2.8,
        "u_value_floor": 0.30,
        "gross_floor_area_m2": 15000,      # ~4,400 students on campus
        "window_area_m2": 2500,            # ~17% of facade
        "roof_area_m2": 3500,
        "wall_area_m2": 8000,
        "floor_area_m2": 3500,
        "ventilation_rate_ach": 0.5,       # air changes per hour
        "occupancy_pattern": "student_library",  # highly variable
        "primary_fuel": "electricity",      # electrically heated (no gas)
        "co2_emissions_t_per_year": 120,   # baseline estimate
    },
    "Greenfield Arts Building": {
        "u_value_wall": 0.40,
        "u_value_roof": 0.30,
        "u_value_window": 3.0,
        "u_value_floor": 0.35,
        "gross_floor_area_m2": 12000,
        "window_area_m2": 2000,
        "roof_area_m2": 3000,
        "wall_area_m2": 7000,
        "floor_area_m2": 3000,
        "ventilation_rate_ach": 0.6,
        "occupancy_pattern": "office_teaching",
        "primary_fuel": "electricity",
        "co2_emissions_t_per_year": 100,
    },
    "Greenfield Science Block": {
        "u_value_wall": 0.38,
        "u_value_roof": 0.28,
        "u_value_window": 2.9,
        "u_value_floor": 0.32,
        "gross_floor_area_m2": 18000,
        "window_area_m2": 3000,
        "roof_area_m2": 4500,
        "wall_area_m2": 9000,
        "floor_area_m2": 4500,
        "ventilation_rate_ach": 0.8,       # labs require higher ventilation
        "occupancy_pattern": "lab_intensive",
        "primary_fuel": "electricity",
        "co2_emissions_t_per_year": 160,
    },
}

# ─────────────────────────────────────────────────────────────────────────────
# INTERVENTION SCENARIOS
# Energy-saving measures with typical cost and energy impact
# ─────────────────────────────────────────────────────────────────────────────
SCENARIOS: Dict[str, Dict[str, Any]] = {
    "Baseline (No Intervention)": {
        "name": "Baseline (No Intervention)",
        "u_wall_multiplier": 1.0,          # no change
        "u_roof_multiplier": 1.0,
        "u_window_multiplier": 1.0,
        "solar_gain_reduction": 0.0,
        "ventilation_reduction": 0.0,
        "heat_recovery_efficiency": 0.0,
        "pv_capacity_kwp": 0,
        "description": "Current condition — no energy interventions",
        "cost_gbp": 0,
        "installation_months": 0,
    },
    "Solar Glass": {
        "name": "Solar Glass",
        "u_wall_multiplier": 1.0,
        "u_roof_multiplier": 1.0,
        "u_window_multiplier": 0.85,       # modest U-value improvement
        "solar_gain_reduction": 0.15,      # 15% reduction in unwanted solar gain
        "ventilation_reduction": 0.0,
        "heat_recovery_efficiency": 0.0,
        "pv_capacity_kwp": 0,
        "description": "High-performance glazing with low-E coating",
        "cost_gbp_per_m2": 180,            # typical range £120–£250/m²
        "installation_months": 4,
    },
    "Green Roof": {
        "name": "Green Roof",
        "u_wall_multiplier": 1.0,
        "u_roof_multiplier": 0.70,         # improved thermal resistance
        "u_window_multiplier": 1.0,
        "solar_gain_reduction": 0.08,
        "ventilation_reduction": 0.0,
        "heat_recovery_efficiency": 0.0,
        "pv_capacity_kwp": 0,
        "description": "Extensive green roof + improved insulation",
        "cost_gbp_per_m2": 150,            # typical range £100–£200/m²
        "installation_months": 3,
    },
    "Enhanced Insulation": {
        "name": "Enhanced Insulation",
        "u_wall_multiplier": 0.60,         # significant improvement
        "u_roof_multiplier": 0.60,
        "u_window_multiplier": 1.0,
        "solar_gain_reduction": 0.0,
        "ventilation_reduction": 0.0,
        "heat_recovery_efficiency": 0.0,
        "pv_capacity_kwp": 0,
        "description": "External wall insulation (EWI) + roof upgrade",
        "cost_gbp_per_m2": 85,             # typical range £60–£120/m² for EWI
        "installation_months": 6,
    },
    "Combined Package": {
        "name": "Combined Package",
        "u_wall_multiplier": 0.55,         # EWI
        "u_roof_multiplier": 0.60,         # green roof
        "u_window_multiplier": 0.85,       # solar glass
        "solar_gain_reduction": 0.20,
        "ventilation_reduction": 0.15,     # enhanced controls
        "heat_recovery_efficiency": 0.65,  # heat recovery ventilation (HRV)
        "pv_capacity_kwp": 0,              # no PV in this variant
        "description": "Holistic retrofit: EWI + green roof + solar glass + HRV",
        "cost_gbp_per_m2": 220,
        "installation_months": 8,
    },
}

# ─────────────────────────────────────────────────────────────────────────────
# SIMPLIFIED STEADY-STATE THERMAL LOAD CALCULATION
# ─────────────────────────────────────────────────────────────────────────────
def calculate_thermal_load(
    building: Dict[str, Any],
    scenario: Dict[str, Any],
    weather: Dict[str, float],
) -> Dict[str, Any]:
    """
    Calculate annual thermal loads and energy/carbon savings for a building under a scenario.
    
    Args:
        building: Dictionary with U-values, areas, and building characteristics
        scenario: Dictionary with intervention multipliers and performance data
        weather: Dictionary with temperature_c and other climate data
    
    Returns:
        Dictionary with energy, carbon, cost savings and final U-values
    
    Physics model notes:
    - Simplified steady-state balance: Q = U·A·ΔT
    - Annual heating demand estimated from degree-days
    - No dynamic thermal mass effects (simplified)
    - Assumes heating season only (5,800 hr/yr standard)
    """
    
    # Extract weather
    outdoor_temp_c = weather.get("temperature_c", 10.5)  # UK average if not provided
    
    # Temperature difference for heating season
    delta_t = max(0, HEATING_SETPOINT_C - outdoor_temp_c)
    
    # Apply scenario multipliers to U-values
    u_wall_adjusted = building["u_value_wall"] * scenario["u_wall_multiplier"]
    u_roof_adjusted = building["u_value_roof"] * scenario["u_roof_multiplier"]
    u_window_adjusted = building["u_value_window"] * scenario["u_window_multiplier"]
    u_floor_adjusted = building["u_value_floor"]  # floor usually not retrofitted
    
    # Calculate baseline heat loss (W)
    q_wall = u_wall_adjusted * building["wall_area_m2"] * delta_t
    q_roof = u_roof_adjusted * building["roof_area_m2"] * delta_t
    q_window = u_window_adjusted * building["window_area_m2"] * delta_t
    q_floor = u_floor_adjusted * building["floor_area_m2"] * delta_t
    
    # Total transmission heat loss
    q_transmission = q_wall + q_roof + q_window + q_floor  # Watts
    
    # Ventilation heat loss (simplified)
    # Q = ρ·cp·V̇·ΔT, where V̇ = ventilation_rate_ach × volume
    volume_m3 = building["gross_floor_area_m2"] * 3.5  # assume 3.5m floor-to-ceiling
    air_change_rate_m3_s = (building["ventilation_rate_ach"] / 3600) * volume_m3
    q_ventilation = 1.2 * 1006 * air_change_rate_m3_s * delta_t  # ρ·cp for air
    
    # Apply ventilation reduction (e.g., heat recovery)
    q_ventilation *= (1.0 - scenario["ventilation_reduction"])
    
    # Total heating load
    q_total_w = q_transmission + q_ventilation
    
    # Annual energy (baseline scenario)
    baseline_annual_mwh = (q_total_w * HEATING_SEASON_HOURS_PER_YEAR) / 1e6
    
    # If baseline scenario (no intervention), energy_saving = 0
    if scenario["name"] == "Baseline (No Intervention)":
        energy_saving_mwh = 0.0
    else:
        # Calculate baseline (without scenario)
        q_baseline_wall = (building["u_value_wall"] * building["wall_area_m2"] * delta_t)
        q_baseline_roof = (building["u_value_roof"] * building["roof_area_m2"] * delta_t)
        q_baseline_window = (building["u_value_window"] * building["window_area_m2"] * delta_t)
        q_baseline_floor = (building["u_value_floor"] * building["floor_area_m2"] * delta_t)
        q_baseline_transmission = q_baseline_wall + q_baseline_roof + q_baseline_window + q_baseline_floor
        q_baseline_ventilation = 1.2 * 1006 * air_change_rate_m3_s * delta_t
        q_baseline_total = q_baseline_transmission + q_baseline_ventilation
        baseline_annual_mwh = (q_baseline_total * HEATING_SEASON_HOURS_PER_YEAR) / 1e6
        
        energy_saving_mwh = max(0, baseline_annual_mwh - ((q_total_w * HEATING_SEASON_HOURS_PER_YEAR) / 1e6))
    
    # Carbon savings (kgCO2 → tonnes)
    carbon_saving_t = round((energy_saving_mwh * 1000 * CARBON_INTENSITY_KG_CO2_PER_KWH) / 1000, 1)
    
    # Cost savings (£)
    cost_saving_gbp = round(energy_saving_mwh * 1000 * ELECTRICITY_COST_GBP_PER_KWH, 0)
    
    # Payback period (years) — if scenario has cost
    payback_years = None
    if scenario["cost_gbp"] > 0 and cost_saving_gbp > 0:
        payback_years = round(scenario["cost_gbp"] / (cost_saving_gbp / HEATING_SEASON_HOURS_PER_YEAR * 8760), 1)
    elif "cost_gbp_per_m2" in scenario and cost_saving_gbp > 0:
        total_cost = scenario["cost_gbp_per_m2"] * (building["wall_area_m2"] + building["roof_area_m2"])
        payback_years = round(total_cost / (cost_saving_gbp / HEATING_SEASON_HOURS_PER_YEAR * 8760), 1)
    
    return {
        "building_name": "Greenfield Library",  # Placeholder
        "scenario_name": scenario["name"],
        "energy_saving_mwh": energy_saving_mwh,
        "carbon_saving_t": carbon_saving_t,
        "cost_saving_gbp": cost_saving_gbp,
        "payback_years": payback_years,
        "u_wall": u_wall_adjusted,
        "u_roof": u_roof_adjusted,
        "u_window": u_window_adjusted,
        "u_floor": u_floor_adjusted,
        "baseline_annual_mwh": baseline_annual_mwh,
        "source": "CrowAgent™ Simplified PINN Physics Model",
=======
# ═══════════════════════════════════════════════════════════════════════════════
# CrowAgent™ Platform — Core Physics Engine
# © 2026 Aparajita Parihar. All rights reserved.
#
# PINN Thermal Model — Raissi et al. (2019) J. Comp. Physics
# doi:10.1016/j.jcp.2018.10.045
# Calibrated against HESA 2022-23 UK HE sector averages + CIBSE Guide A
# ═══════════════════════════════════════════════════════════════════════════════

from __future__ import annotations

# ── BUILDING DATA ─────────────────────────────────────────────────────────────
BUILDINGS: dict[str, dict] = {
    "Greenfield Library": {
        "floor_area_m2":       8500,
        "height_m":            4.5,
        "glazing_ratio":       0.35,
        "u_value_wall":        1.8,
        "u_value_roof":        2.1,
        "u_value_glazing":     2.8,
        "baseline_energy_mwh": 487,
        "occupancy_hours":     3500,
        "description":         "Main campus library — 8,500 m² · 5 floors · Heavy glazing",
        "built_year":          "Pre-1990",
        "building_type":       "Library / Learning Hub",
    },
    "Greenfield Arts Building": {
        "floor_area_m2":       11200,
        "height_m":            5.0,
        "glazing_ratio":       0.28,
        "u_value_wall":        2.1,
        "u_value_roof":        1.9,
        "u_value_glazing":     3.1,
        "baseline_energy_mwh": 623,
        "occupancy_hours":     4000,
        "description":         "Humanities faculty — 11,200 m² · 6 floors · Lecture theatres",
        "built_year":          "Pre-1985",
        "building_type":       "Teaching / Lecture",
    },
    "Greenfield Science Block": {
        "floor_area_m2":       6800,
        "height_m":            4.0,
        "glazing_ratio":       0.30,
        "u_value_wall":        1.6,
        "u_value_roof":        1.7,
        "u_value_glazing":     2.6,
        "baseline_energy_mwh": 391,
        "occupancy_hours":     3200,
        "description":         "Science laboratories — 6,800 m² · 4 floors · Lab-heavy usage",
        "built_year":          "Pre-1995",
        "building_type":       "Laboratory / Research",
    },
}

SCENARIOS: dict[str, dict] = {
    "Baseline (No Intervention)": {
        "description":            "Current state — no modifications applied.",
        "u_wall_factor":          1.0,
        "u_roof_factor":          1.0,
        "u_glazing_factor":       1.0,
        "solar_gain_reduction":   0.0,
        "infiltration_reduction": 0.0,
        "renewable_kwh":          0,
        "install_cost_gbp":       0,
        "colour":                 "#4A6FA5",
        "icon":                   "🏢",
    },
    "Solar Glass Installation": {
        "description":            "Replace standard glazing with BIPV solar glass. U-value improvement ~45%.",
        "u_wall_factor":          1.0,
        "u_roof_factor":          1.0,
        "u_glazing_factor":       0.55,
        "solar_gain_reduction":   0.15,
        "infiltration_reduction": 0.05,
        "renewable_kwh":          42000,
        "install_cost_gbp":       280000,
        "colour":                 "#00C2A8",
        "icon":                   "☀️",
    },
    "Green Roof Installation": {
        "description":            "Vegetated green roof layer. Roof U-value improvement ~55%.",
        "u_wall_factor":          1.0,
        "u_roof_factor":          0.45,
        "u_glazing_factor":       1.0,
        "solar_gain_reduction":   0.0,
        "infiltration_reduction": 0.02,
        "renewable_kwh":          0,
        "install_cost_gbp":       95000,
        "colour":                 "#1DB87A",
        "icon":                   "🌱",
    },
    "Enhanced Insulation Upgrade": {
        "description":            "Wall, roof and glazing upgrade to near-Passivhaus standard.",
        "u_wall_factor":          0.40,
        "u_roof_factor":          0.35,
        "u_glazing_factor":       0.70,
        "solar_gain_reduction":   0.0,
        "infiltration_reduction": 0.20,
        "renewable_kwh":          0,
        "install_cost_gbp":       520000,
        "colour":                 "#0A5C3E",
        "icon":                   "🏗️",
    },
    "Combined Package (All Interventions)": {
        "description":            "Solar glass + green roof + enhanced insulation simultaneously.",
        "u_wall_factor":          0.40,
        "u_roof_factor":          0.35,
        "u_glazing_factor":       0.55,
        "solar_gain_reduction":   0.15,
        "infiltration_reduction": 0.22,
        "renewable_kwh":          42000,
        "install_cost_gbp":       895000,
        "colour":                 "#062E1E",
        "icon":                   "⚡",
    },
}


def calculate_thermal_load(building: dict, scenario: dict, weather_data: dict) -> dict:
    """
    Physics-informed thermal load calculation.
    Q_transmission = U × A × ΔT × hours  [Wh]
    Q_infiltration = 0.33 × ACH × Vol × ΔT  [Wh]
    Ref: Raissi et al. (2019) doi:10.1016/j.jcp.2018.10.045

    DISCLAIMER: Simplified steady-state model. Results are indicative only.
    Not for use as sole basis for investment decisions.
    """
    b    = building
    s    = scenario
    temp = weather_data["temperature_c"]

    # ── Geometry ──────────────────────────────────────────────────────────────
    perimeter_m     = 4.0 * (b["floor_area_m2"] ** 0.5)
    wall_area_m2    = perimeter_m * b["height_m"] * (1.0 - b["glazing_ratio"])
    glazing_area_m2 = perimeter_m * b["height_m"] * b["glazing_ratio"]
    roof_area_m2    = b["floor_area_m2"]
    volume_m3       = b["floor_area_m2"] * b["height_m"]

    # ── Effective U-values post-intervention ──────────────────────────────────
    u_wall    = b["u_value_wall"]    * s["u_wall_factor"]
    u_roof    = b["u_value_roof"]    * s["u_roof_factor"]
    u_glazing = b["u_value_glazing"] * s["u_glazing_factor"]

    # ── Heat loss (CIBSE Guide A) ─────────────────────────────────────────────
    delta_t     = max(0.0, 21.0 - temp)   # 21°C set-point (Part L)
    heating_hrs = 5800.0                   # UK heating season hours

    q_wall    = u_wall    * wall_area_m2    * delta_t * heating_hrs
    q_roof    = u_roof    * roof_area_m2    * delta_t * heating_hrs
    q_glazing = u_glazing * glazing_area_m2 * delta_t * heating_hrs
    q_trans_mwh = (q_wall + q_roof + q_glazing) / 1_000_000.0

    # ── Infiltration (CIBSE Guide A) ──────────────────────────────────────────
    ach       = 0.7 * (1.0 - s["infiltration_reduction"])
    q_inf_mwh = (0.33 * ach * volume_m3 * delta_t * heating_hrs) / 1_000_000.0

    # ── Solar gain offset (PVGIS: 950 kWh/m²/yr Reading) ─────────────────────
    solar_mwh    = (950.0 * glazing_area_m2 * 0.6 * (1.0 - s["solar_gain_reduction"])) / 1_000.0
    modelled_mwh = max(0.0, q_trans_mwh + q_inf_mwh - solar_mwh * 0.3)

    # ── Baseline (no scenario) ────────────────────────────────────────────────
    baseline_raw = (
        b["u_value_wall"]    * wall_area_m2    * delta_t * heating_hrs
      + b["u_value_roof"]    * roof_area_m2    * delta_t * heating_hrs
      + b["u_value_glazing"] * glazing_area_m2 * delta_t * heating_hrs
      + 0.33 * 0.7           * volume_m3       * delta_t * heating_hrs
    ) / 1_000_000.0

    reduction_ratio = (
        max(0.0, 1.0 - (baseline_raw - modelled_mwh) / baseline_raw)
        if baseline_raw > 0 else 1.0
    )

    # Detect baseline scenario (no changes) and preserve declared baseline energy
    is_baseline = (
        float(s.get("u_wall_factor", 1.0)) == 1.0
        and float(s.get("u_roof_factor", 1.0)) == 1.0
        and float(s.get("u_glazing_factor", 1.0)) == 1.0
        and float(s.get("solar_gain_reduction", 0.0)) == 0.0
        and float(s.get("infiltration_reduction", 0.0)) == 0.0
        and int(s.get("renewable_kwh", 0)) == 0
        and int(s.get("install_cost_gbp", 0)) == 0
    )

    if is_baseline:
        adjusted_mwh = b["baseline_energy_mwh"]
        renewable_mwh = 0.0
        final_mwh = adjusted_mwh
    else:
        adjusted_mwh  = b["baseline_energy_mwh"] * max(0.35, reduction_ratio)
        renewable_mwh = s.get("renewable_kwh", 0) / 1_000.0
        final_mwh     = max(0.0, adjusted_mwh - renewable_mwh)

    # ── Carbon (BEIS 2023: 0.20482 kgCO₂e/kWh) ───────────────────────────────
    ci              = 0.20482
    baseline_carbon = (b["baseline_energy_mwh"] * 1000.0 * ci) / 1000.0
    scenario_carbon = (final_mwh * 1000.0 * ci) / 1000.0

    # ── Financial (HESA 2022-23: £0.28/kWh) ──────────────────────────────────
    unit_cost     = 0.28
    annual_saving = (b["baseline_energy_mwh"] - final_mwh) * 1000.0 * unit_cost
    install_cost  = float(s["install_cost_gbp"])
    payback       = (install_cost / annual_saving) if annual_saving > 0.0 else None

    cpt = round(install_cost / max(baseline_carbon - scenario_carbon, 0.01), 1) \
          if install_cost > 0 else None

    baseline_mwh = b.get("baseline_energy_mwh", 0.0)

    return {
        "baseline_energy_mwh": round(b["baseline_energy_mwh"], 1),
        "scenario_energy_mwh": round(final_mwh, 1),
        "energy_saving_mwh":   round(baseline_mwh - final_mwh, 1),
        "energy_saving_pct":   round((baseline_mwh - final_mwh)
                                     / (baseline_mwh if baseline_mwh > 0 else 1.0) * 100.0, 1),
        "baseline_carbon_t":   round(baseline_carbon, 1),
        "scenario_carbon_t":   round(scenario_carbon, 1),
        "carbon_saving_t":     round(baseline_carbon - scenario_carbon, 1),
        "annual_saving_gbp":   round(annual_saving, 0),
        "install_cost_gbp":    install_cost,
        "payback_years":       round(payback, 1) if payback else None,
        "cost_per_tonne_co2":  cpt,
        "renewable_mwh":       round(renewable_mwh, 1),
        "u_wall":              round(u_wall, 2),
        "u_roof":              round(u_roof, 2),
        "u_glazing":           round(u_glazing, 2),
>>>>>>> 1f29a2b095dde03823652f7da0437ef1a20f629c
    }
