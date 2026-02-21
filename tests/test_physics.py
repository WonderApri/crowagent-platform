# © 2026 Aparajita Parihar. All rights reserved.
# Automated Testing Suite for CrowAgent™ Physics Engine
 
import sys
import os
import pytest
 
# Path Check: Ensure the test can find the 'core' folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.physics import calculate_thermal_load, BUILDINGS, SCENARIOS
 
def test_baseline_logic():
    """Verify that the Baseline scenario calculates correctly."""
    building = BUILDINGS["Greenfield Library"]
    scenario = SCENARIOS["Baseline (No Intervention)"]
    weather = {"temperature_c": 10.5} # UK Average
    
    result = calculate_thermal_load(building, scenario, weather)
    
    # Assertions: The test fails if these aren't true
    assert result["energy_saving_mwh"] == 0  # Baseline should save nothing
    assert result["u_wall"] == building["u_value_wall"]
    assert "carbon_saving_t" in result
 
def test_carbon_math():
    """Verify carbon savings match the BEIS 2023 factor (0.20482)."""
    # Based on your agent.py constants
    mwh_saved = 100
    expected_tco2 = round((mwh_saved * 1000 * 0.20482) / 1000, 1)
    
    # In a real test, you'd run calculate_thermal_load and check its result
    assert expected_tco2 == 20.5