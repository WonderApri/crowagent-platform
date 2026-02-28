# ═══════════════════════════════════════════════════════════════════════════════
# CrowAgent™ Platform — Segment Handler Abstract Base Class
# © 2026 Aparajita Parihar. All rights reserved.
#
# Architecture rule:
#   Zero Streamlit imports permitted in this file or any SegmentHandler subclass.
#   Segment handlers are pure data/configuration providers.
#   All rendering is the responsibility of app/tabs/*.py modules.
# ═══════════════════════════════════════════════════════════════════════════════

from __future__ import annotations

import abc


class SegmentHandler(abc.ABC):
    """Abstract base class for all CrowAgent user-segment handlers.

    Concrete subclasses provide building registries, scenario whitelists,
    and compliance metadata for a specific customer segment.  They contain
    NO rendering logic and import NO Streamlit symbols.
    """

    # ── Abstract properties ───────────────────────────────────────────────────

    @property
    @abc.abstractmethod
    def segment_id(self) -> str:
        """Canonical snake_case segment identifier (e.g. 'university_he')."""

    @property
    @abc.abstractmethod
    def display_label(self) -> str:
        """Human-readable label with emoji prefix (e.g. '🏛️ University / HE')."""

    @property
    @abc.abstractmethod
    def building_registry(self) -> dict[str, dict]:
        """Dict mapping building name → building specification dict.

        Each value must contain at minimum:
          floor_area_m2, height_m, glazing_ratio,
          u_value_wall, u_value_roof, u_value_glazing,
          baseline_energy_mwh, occupancy_hours, description,
          built_year, building_type.
        """

    @property
    @abc.abstractmethod
    def scenario_whitelist(self) -> list[str]:
        """Ordered list of scenario names available to this segment.

        Every entry must be a key in config.scenarios.SCENARIOS.
        """

    @property
    @abc.abstractmethod
    def default_scenarios(self) -> list[str]:
        """Scenario names pre-selected on first load.

        Must be a subset of scenario_whitelist.
        """

    @property
    @abc.abstractmethod
    def compliance_checks(self) -> list[str]:
        """Compliance module IDs relevant to this segment.

        Valid values: 'epc_mees', 'part_l', 'fhs', 'secr'.
        """

    # ── Concrete methods ──────────────────────────────────────────────────────

    def get_building(self, name: str) -> dict:
        """Return the building spec for *name* from this segment's registry.

        Raises:
            KeyError: if *name* is not present in building_registry.
        """
        if name not in self.building_registry:
            raise KeyError(
                f"Building {name!r} not found in {self.segment_id!r} registry. "
                f"Available: {list(self.building_registry)}"
            )
        return self.building_registry[name]
