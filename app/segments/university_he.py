# ═══════════════════════════════════════════════════════════════════════════════
# CrowAgent™ Platform — University / Higher Education Segment Handler
# © 2026 Aparajita Parihar. All rights reserved.
#
# Building data: Greenfield University (FICTIONAL — for demonstration only).
# All figures derived from published UK HE sector averages (HESA 2022-23).
# ═══════════════════════════════════════════════════════════════════════════════

from __future__ import annotations

from config.scenarios import SEGMENT_DEFAULT_SCENARIOS, SEGMENT_SCENARIOS
from .base import SegmentHandler


class UniversityHEHandler(SegmentHandler):
    """Segment handler for University / Higher Education estates."""

    @property
    def segment_id(self) -> str:
        return "university_he"

    @property
    def display_label(self) -> str:
        return "🏛️ University / Higher Education"

    @property
    def building_registry(self) -> dict[str, dict]:
        return {
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

    @property
    def scenario_whitelist(self) -> list[str]:
        return SEGMENT_SCENARIOS["university_he"]

    @property
    def default_scenarios(self) -> list[str]:
        return SEGMENT_DEFAULT_SCENARIOS["university_he"]

    @property
    def compliance_checks(self) -> list[str]:
        return ["epc_mees"]
