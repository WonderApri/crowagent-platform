"""
Batch 6 Acceptance Test: Add smoke tests per segment handler.
"""
from config.scenarios import SCENARIOS
from app.segments import get_segment_handler, SEGMENT_IDS

def test_all_handlers_instantiate_and_are_valid():
    """Ensures all segment handlers load and have valid registries."""
    for sid in SEGMENT_IDS:
        h = get_segment_handler(sid)
        assert len(h.building_registry) > 0, f"{sid} has empty building_registry"
        for name in h.scenario_whitelist:
            assert name in SCENARIOS, f"{sid}: unknown scenario {name}"