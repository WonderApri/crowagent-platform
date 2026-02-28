from .base import SegmentHandler

class CommercialLandlordHandler(SegmentHandler):
    display_label = "🏢 Commercial Landlord"
    building_registry = {"Office Block A": {"floor_area_m2": 1200}}