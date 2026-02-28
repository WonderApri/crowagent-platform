from .university_he import UniversityHEHandler
from .commercial_landlord import CommercialLandlordHandler
from .smb_industrial import SMBIndustrialHandler
from .individual_selfbuild import IndividualSelfBuildHandler

SEGMENT_LABELS = {
    "university_he": "🏛️ University / HE",
    "smb_landlord": "🏢 Commercial Landlord",
    "smb_industrial": "🏭 SMB Industrial",
    "individual_selfbuild": "🏠 Individual Self-Build",
}

def get_segment_handler(segment_id):
    registry = {
        "university_he": UniversityHEHandler,
        "smb_landlord": CommercialLandlordHandler,
        "smb_industrial": SMBIndustrialHandler,
        "individual_selfbuild": IndividualSelfBuildHandler,
    }
    handler_cls = registry.get(segment_id)
    if not handler_cls:
        raise ValueError(f"Unknown segment: {segment_id}")
    return handler_cls()