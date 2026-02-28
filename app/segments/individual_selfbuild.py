# ═══════════════════════════════════════════════════════════════════════════════
# CrowAgent™ Platform — Individual Self-Build Segment Handler
# © 2026 Aparajita Parihar. All rights reserved.
#
# Building data sourced from app/compliance.py SEGMENT_BUILDINGS["individual_selfbuild"].
# ═══════════════════════════════════════════════════════════════════════════════

from __future__ import annotations

from config.scenarios import SEGMENT_DEFAULT_SCENARIOS, SEGMENT_SCENARIOS
from .base import SegmentHandler


class IndividualSelfBuildHandler(SegmentHandler):
    """Segment handler for Individual Self-Build projects (Part L / FHS compliance)."""

    @property
    def segment_id(self) -> str:
        return "individual_selfbuild"

    @property
    def display_label(self) -> str:
        return "🏠 Individual Self-Build"

    @property
    def building_registry(self) -> dict[str, dict]:
        return {
            "Example Self-Build — 3-Bed Detached (120 m²)": {
                "floor_area_m2":       120,
                "height_m":            2.7,
                "glazing_ratio":       0.20,
                "u_value_wall":        1.6,
                "u_value_roof":        2.0,
                "u_value_glazing":     2.8,
                "baseline_energy_mwh": 18.0,
                "occupancy_hours":     5500,
                "description":         "Typical self-build 3-bed detached — 120 m² · Pre-Part L 2021",
                "built_year":          "Pre-2021",
                "building_type":       "Residential / Self-Build",
                "segment":             "individual_selfbuild",
            },
            "Example Self-Build — 2-Bed Semi-Detached (85 m²)": {
                "floor_area_m2":       85,
                "height_m":            2.6,
                "glazing_ratio":       0.18,
                "u_value_wall":        1.8,
                "u_value_roof":        2.2,
                "u_value_glazing":     3.0,
                "baseline_energy_mwh": 12.5,
                "occupancy_hours":     5500,
                "description":         "Typical self-build 2-bed semi — 85 m² · Pre-Part L 2021",
                "built_year":          "Pre-2021",
                "building_type":       "Residential / Self-Build",
                "segment":             "individual_selfbuild",
            },
        }

    @property
    def scenario_whitelist(self) -> list[str]:
        return SEGMENT_SCENARIOS["individual_selfbuild"]

    @property
    def default_scenarios(self) -> list[str]:
        return SEGMENT_DEFAULT_SCENARIOS["individual_selfbuild"]

    @property
    def compliance_checks(self) -> list[str]:
        return ["part_l", "fhs"]
