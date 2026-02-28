# ═══════════════════════════════════════════════════════════════════════════════
# CrowAgent™ Platform — Segment Package
# © 2026 Aparajita Parihar. All rights reserved.
#
# Public API:
#   get_segment_handler(segment_id) -> SegmentHandler
#   SEGMENT_IDS   : list[str]
#   SEGMENT_LABELS: dict[str, str]
# ═══════════════════════════════════════════════════════════════════════════════

from __future__ import annotations

import importlib

from .base import SegmentHandler

# Lazy class loading map — defers import until first use.
_MODULE_MAP: dict[str, tuple[str, str]] = {
    "university_he":        ("app.segments.university_he",        "UniversityHEHandler"),
    "smb_landlord":         ("app.segments.commercial_landlord",  "CommercialLandlordHandler"),
    "smb_industrial":       ("app.segments.smb_industrial",       "SMBIndustrialHandler"),
    "individual_selfbuild": ("app.segments.individual_selfbuild", "IndividualSelfBuildHandler"),
}

SEGMENT_IDS: list[str] = list(_MODULE_MAP)

SEGMENT_LABELS: dict[str, str] = {
    "university_he":        "🏛️ University / Higher Education",
    "smb_landlord":         "🏢 Commercial Landlord",
    "smb_industrial":       "🏭 SMB Industrial",
    "individual_selfbuild": "🏠 Individual Self-Build",
}


def get_segment_handler(segment_id: str) -> SegmentHandler:
    """Return an instantiated SegmentHandler for the given segment ID.

    Args:
        segment_id: One of the keys in SEGMENT_IDS.

    Returns:
        An instance of the appropriate SegmentHandler subclass.

    Raises:
        KeyError: if segment_id is not a recognised segment.
    """
    if segment_id not in _MODULE_MAP:
        raise KeyError(
            f"Unknown segment ID {segment_id!r}. "
            f"Valid IDs: {SEGMENT_IDS}"
        )
    module_path, class_name = _MODULE_MAP[segment_id]
    module = importlib.import_module(module_path)
    cls = getattr(module, class_name)
    return cls()


__all__ = ["SegmentHandler", "get_segment_handler", "SEGMENT_IDS", "SEGMENT_LABELS"]
