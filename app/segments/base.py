# ═══════════════════════════════════════════════════════════════════════════════
# CrowAgent™ Platform — Segment Handler Abstract Base Class
# © 2026 Aparajita Parihar. All rights reserved.
#
# This module defines the abstract interface (contract) that all user-facing
# business segments must implement. This ensures that the main application can
# interact with any segment in a consistent, polymorphic way, without needing
# segment-specific `if/elif` blocks.
#
# The design enforces a strict separation of concerns:
#   - Segment modules own their specific building templates, scenario whitelists,
#     and compliance check requirements.
#   - The main application and tab renderers consume this data without knowing
#     the implementation details of any specific segment.
#
# This file must have ZERO Streamlit or network-related imports. It is a pure
# Python module defining a data contract.
# ═══════════════════════════════════════════════════════════════════════════════

from __future__ import annotations

import abc
from typing import ClassVar, Type

class SegmentHandler(abc.ABC):
    """
    Abstract Base Class for a user-facing business segment.

    Each implementation of this class represents a distinct application vertical
    (e.g., University/HE, Commercial Landlord) and provides the necessary
    data and metadata for the UI and physics engine to function correctly for
    that vertical.
    """

    @property
    @abc.abstractmethod
    def segment_id(self) -> str:
        """A unique, URL-safe identifier for the segment (e.g., 'university_he')."""
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def display_label(self) -> str:
        """A user-friendly, displayable name for the segment (e.g., '🏛️ University / Higher Education')."""
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def building_registry(self) -> dict[str, dict]:
        """
        A dictionary of building templates available for this segment.
        The keys are the user-facing names of the buildings.
        The values are dictionaries matching the `BuildingDict` structure required by `core.physics`.
        """
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def scenario_whitelist(self) -> list[str]:
        """
        A list of scenario names (keys from `config.scenarios.SCENARIOS`)
        that are permitted for use within this segment.
        """
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def default_scenarios(self) -> list[str]:
        """
        A list of scenario names that should be pre-selected by default when
        a user enters this segment for the first time.
        """
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def compliance_checks(self) -> list[str]:
        """
        A list of identifiers for compliance checks relevant to this segment.
        These keys (e.g., 'epc_mees', 'part_l') determine which panels are
        rendered in the 'UK Compliance Hub' tab.
        """
        raise NotImplementedError

    def get_building(self, name: str) -> dict:
        """
        Retrieves a specific building template by its name.

        Args:
            name: The name of the building to retrieve.

        Returns:
            The building data dictionary.

        Raises:
            KeyError: If no building with the specified name exists in the registry.
        """
        try:
            return self.building_registry[name]
        except KeyError:
            raise KeyError(
                f"Building '{name}' not found in the '{self.display_label}' segment registry. "
                f"Available buildings are: {list(self.building_registry.keys())}"
            )
