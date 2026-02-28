# ═══════════════════════════════════════════════════════════════════════════════
# CrowAgent™ Platform — Commercial Landlord Segment Handler
# © 2026 Aparajita Parihar. All rights reserved.
# ═══════════════════════════════════════════════════════════════════════════════

from __future__ import annotations

from config.scenarios import SEGMENT_DEFAULT_SCENARIOS, SEGMENT_SCENARIOS
from .base import SegmentHandler


class CommercialLandlordHandler(SegmentHandler):
    """Segment handler for SMB Commercial Landlords (MEES compliance)."""

    @property
    def segment_id(self) -> str:
        return "commercial_landlord"

    @property
    def display_label(self) -> str:
        return "🏢 Commercial Landlord"

    @property
    def building_registry(self) -> dict[str, dict]:
        return {
            "Example Office Unit (500 m²)": {
                "floor_area_m2":       500,
                "height_m":            3.2,
                "glazing_ratio":       0.35,
                "u_value_wall":        1.7,
                "u_value_roof":        1.8,
                "u_value_glazing":     2.8,
                "baseline_energy_mwh": 72.0,
                "occupancy_hours":     2500,
                "description":         "SMB office — 500 m² · Typical pre-2010 commercial fit-out",
                "built_year":          "Pre-2010",
                "building_type":       "Office / Commercial",
                "segment":             "commercial_landlord",
            },
            "Example Retail Unit (200 m²)": {
                "floor_area_m2":       200,
                "height_m":            3.5,
                "glazing_ratio":       0.50,
                "u_value_wall":        2.0,
                "u_value_roof":        2.1,
                "u_value_glazing":     3.1,
                "baseline_energy_mwh": 38.0,
                "occupancy_hours":     3000,
                "description":         "SMB retail unit — 200 m² · High glazing frontage",
                "built_year":          "Pre-2005",
                "building_type":       "Retail / Shopfront",
                "segment":             "commercial_landlord",
            },
            "Example Light Industrial Unit (1,200 m²)": {
                "floor_area_m2":       1200,
                "height_m":            6.0,
                "glazing_ratio":       0.12,
                "u_value_wall":        1.9,
                "u_value_roof":        2.3,
                "u_value_glazing":     2.6,
                "baseline_energy_mwh": 145.0,
                "occupancy_hours":     3000,
                "description":         "SMB light industrial — 1,200 m² · Single-skin metal cladding",
                "built_year":          "Pre-2000",
                "building_type":       "Industrial / Warehouse",
                "segment":             "commercial_landlord",
            },
        }

    @property
    def scenario_whitelist(self) -> list[str]:
        return SEGMENT_SCENARIOS["commercial_landlord"]

    @property
    def default_scenarios(self) -> list[str]:
        return SEGMENT_DEFAULT_SCENARIOS["commercial_landlord"]

    @property
    def compliance_checks(self) -> list[str]:
        return ["epc_mees", "part_l"]
