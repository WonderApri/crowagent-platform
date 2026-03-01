SEGMENT_LABELS = {
    "university_he": "🏛️ University / Higher Education",
    "smb_landlord": "🏢 Commercial Landlord",
    "smb_industrial": "🏭 SMB Industrial",
    "individual_selfbuild": "🏠 Individual Self-Build"
}

SEGMENT_IDS = list(SEGMENT_LABELS.keys())

def get_segment_handler(segment_id):
    class Handler:
        def __init__(self):
            self.building_registry = {}
            self.scenario_whitelist = []
            self.compliance_checks = []
    return Handler()