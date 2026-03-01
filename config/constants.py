"""
Physical and financial constants.
Canonical source of truth for the platform.
"""

# ─────────────────────────────────────────────────────────────────────────────
# Physical Constants (sourced from core/physics.py)
# ─────────────────────────────────────────────────────────────────────────────
DEFAULT_ELECTRICITY_TARIFF_GBP_PER_KWH = 0.28
HEATING_SETPOINT_C = 21.0
HEATING_HOURS_PER_YEAR = 5800.0
BASE_ACH = 0.5  # Standard baseline air changes per hour
SOLAR_IRRADIANCE_KWH_M2_YEAR = 950.0
SOLAR_APERTURE_FACTOR = 1.0
SOLAR_UTILISATION_FACTOR = 1.0

# ─────────────────────────────────────────────────────────────────────────────
# Compliance Constants (sourced from app/compliance.py)
# ─────────────────────────────────────────────────────────────────────────────
CI_ELECTRICITY = 0.20482
CI_GAS = 0.18316  # Standard BEIS value
CI_OIL = 0.26831  # Standard BEIS value
CI_LPG = 0.21448  # Standard BEIS value

ELEC_COST_PER_KWH = 0.28
GAS_COST_PER_KWH = 0.07

EPC_BANDS = ["A", "B", "C", "D", "E", "F", "G"]
MEES_CURRENT_MIN_BAND = "E"
MEES_2028_TARGET_BAND = "C"
MEES_2030_TARGET_BAND = "B"

PART_L_2021_U_WALL = 0.18
PART_L_2021_U_ROOF = 0.15
PART_L_2021_U_GLAZING = 1.4

FHS_MAX_PRIMARY_ENERGY = 45.0

PART_L_2021_ND_U_WALL = 0.26
PART_L_2021_ND_U_ROOF = 0.18
PART_L_2021_ND_U_GLAZING = 1.6