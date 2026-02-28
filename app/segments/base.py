class SegmentHandler:
    @property
    def display_label(self):
        return "Segment"
        
    @property
    def building_registry(self):
        return {}
        
    def get_building(self, name):
        return {}