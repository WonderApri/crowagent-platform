from .base import SegmentHandler

class IndividualSelfBuildHandler(SegmentHandler):
    display_label = "🏠 Individual Self-Build"
    building_registry = {"Detached House": {"floor_area_m2": 150}}