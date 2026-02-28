# ═══════════════════════════════════════════════════════════════════════════════
# CrowAgent™ Platform — Global Constants
# © 2026 Aparajita Parihar. All rights reserved.
#
# SINGLE SOURCE OF TRUTH for all physical, financial, and regulatory constants.
# As per ARCHITECTURE_FREEZE.md — TASK 002.
# ═══════════════════════════════════════════════════════════════════════════════

from __future__ import annotations

# ─────────────────────────────────────────────────────────────────────────────
# PHYSICAL & CARBON INTENSITY CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────
# BEIS GHG Conversion Factors 2023
CI_ELECTRICITY = 0.20482   # kgCO₂e / kWh — BEIS 2023 UK grid
CI_GAS         = 0.18316   # kgCO₂e / kWh — BEIS 2023 natural gas (Scope 1)
CI_OIL         = 0.24615   # kgCO₂e / kWh — BEIS 2023 gas oil (Scope 1)
CI_LPG         = 0.21435   # kgCO₂e / kWh — BEIS 2023 LPG (Scope 1)

# Physics Model Constants (calibrated against CIBSE Guide A)
HEATING_SETPOINT_C = 20.0                # °C
HEATING_HOURS_PER_YEAR = 3000.0          # Assumed operational hours for heating
INFILTRATION_HEAT_CAPACITY_FACTOR = 0.33 # Volumetric heat capacity of air (J/m³K) / 3600
BASE_ACH = 1.5                           # Air Changes per Hour (baseline, typical non-residential)
SOLAR_IRRADIANCE_KWH_M2_YEAR = 950.0     # Average UK horizontal solar irradiance
SOLAR_APERTURE_FACTOR = 0.85             # Effective aperture vs. glazing area (SHGC)
SOLAR_UTILISATION_FACTOR = 0.9           # Usable portion of solar gains for heating offset

# ─────────────────────────────────────────────────────────────────────────────
# FINANCIAL CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────
# UK energy cost assumptions (Q1 2026 projection, SMB commercial rates)
DEFAULT_ELECTRICITY_TARIFF_GBP_PER_KWH  = 0.28   # £/kWh
DEFAULT_GAS_TARIFF_GBP_PER_KWH   = 0.07   # £/kWh

# ─────────────────────────────────────────────────────────────────────────────
# REGULATORY & COMPLIANCE CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────

# --- SAP/EPC BAND LOOKUP (SAP 10.2 — proxy, indicative only) ---
# Band thresholds: A ≥ 92 · B 81–91 · C 69–80 · D 55–68 · E 39–54 · F 21–38 · G 1–20
EPC_BANDS: list[tuple[int, str, str]] = [
    (92, "A", "#00873D"),
    (81, "B", "#2ECC40"),
    (69, "C", "#85C226"),
    (55, "D", "#F0B429"),
    (39, "E", "#F06623"),
    (21, "F", "#E84C4C"),
    (1,  "G", "#C0392B"),
]

# --- MEES England & Wales thresholds (non-domestic) ---
MEES_CURRENT_MIN_BAND  = "E"   # In force since April 2023
MEES_2028_TARGET_BAND  = "C"   # Planned for new tenancies by 2028
MEES_2030_TARGET_BAND  = "C"   # All leases by 2030 (indicative)

# --- Part L 2021 U-value targets for new dwellings (notional building) ---
PART_L_2021_U_WALL    = 0.18   # W/m²K
PART_L_2021_U_ROOF    = 0.11   # W/m²K
PART_L_2021_U_GLAZING = 1.20   # W/m²K

# --- Future Homes Standard (FHS) 2025/26 indicative target ---
FHS_MAX_PRIMARY_ENERGY = 35    # kWh/m²/yr (approximate — final standard TBC)

# --- Part L 2021 U-value targets for non-domestic (new builds / major renovations) ---
PART_L_2021_ND_U_WALL    = 0.26
PART_L_2021_ND_U_ROOF    = 0.18
PART_L_2021_ND_U_GLAZING = 1.60
