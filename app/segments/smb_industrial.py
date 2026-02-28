# ═══════════════════════════════════════════════════════════════════════════════
# CrowAgent™ Platform — SMB Industrial Segment Handler
# © 2026 Aparajita Parihar. All rights reserved.
#
# Building data sourced from app/compliance.py SEGMENT_BUILDINGS["smb_industrial"].
# ═══════════════════════════════════════════════════════════════════════════════

from __future__ import annotations

from config.scenarios import SEGMENT_DEFAULT_SCENARIOS, SEGMENT_SCENARIOS
from .base import SegmentHandler


class SMBIndustrialHandler(SegmentHandler):
    """Segment handler for SMB Industrial Operators (SECR / carbon baseline)."""

    @property
    def segment_id(self) -> str:
        return "smb_industrial"

    @property
    def display_label(self) -> str:
        return "🏭 SMB Industrial"

    @property
    def building_registry(self) -> dict[str, dict]:
        return {
            "Example Small Manufacturer (2,000 m²)": {
                "floor_area_m2":       2000,
                "height_m":            7.0,
                "glazing_ratio":       0.10,
                "u_value_wall":        2.1,
                "u_value_roof":        2.5,
                "u_value_glazing":     2.8,
                "baseline_energy_mwh": 380.0,
                "occupancy_hours":     4000,
                "description":         "SMB manufacturing — 2,000 m² · Process heat + lighting dominated",
                "built_year":          "Pre-1995",
                "building_type":       "Manufacturing / Industrial",
                "segment":             "smb_industrial",
            },
            "Example Logistics Depot (3,500 m²)": {
                "floor_area_m2":       3500,
                "height_m":            9.0,
                "glazing_ratio":       0.08,
                "u_value_wall":        2.0,
                "u_value_roof":        2.2,
                "u_value_glazing":     2.6,
                "baseline_energy_mwh": 520.0,
                "occupancy_hours":     5000,
                "description":         "SMB logistics — 3,500 m² · High door infiltration, 24hr operation",
                "built_year":          "Pre-2000",
                "building_type":       "Logistics / Depot",
                "segment":             "smb_industrial",
            },
        }

    @property
    def scenario_whitelist(self) -> list[str]:
        return SEGMENT_SCENARIOS["smb_industrial"]

    @property
    def default_scenarios(self) -> list[str]:
        return SEGMENT_DEFAULT_SCENARIOS["smb_industrial"]

    @property
    def compliance_checks(self) -> list[str]:
        return ["secr", "part_l"]
