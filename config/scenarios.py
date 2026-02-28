"""
Scenario definitions and segment whitelists.
"""
SCENARIOS = {
    "Baseline": {"u_wall_factor": 1.0, "u_roof_factor": 1.0, "u_glazing_factor": 1.0, "install_cost_gbp": 0},
    "Fabric Upgrade": {"u_wall_factor": 0.6, "u_roof_factor": 0.6, "u_glazing_factor": 0.4, "install_cost_gbp": 50000},
    "Heat Pump": {"u_wall_factor": 1.0, "u_roof_factor": 1.0, "u_glazing_factor": 1.0, "install_cost_gbp": 12000},
}

SEGMENT_SCENARIOS = {
    "university_he": ["Baseline", "Fabric Upgrade", "Heat Pump"],
    "smb_landlord": ["Baseline", "Fabric Upgrade"],
    "smb_industrial": ["Baseline"],
    "individual_selfbuild": ["Baseline", "Fabric Upgrade", "Heat Pump"],
}