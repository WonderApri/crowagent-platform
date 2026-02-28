"""
Constants for the Streamlit application.
"""

# S3 bucket for assets
S3_BUCKET = "your-s3-bucket-name"

# Asset URLs
CROWAGENT_ICON_SQUARE_URL = f"https://{S3_BUCKET}.s3.amazonaws.com/CrowAgent_Icon_Square.svg"
CROWAGENT_LOGO_HORIZONTAL_DARK_URL = f"https://{S3_BUCKET}.s3.amazonaws.com/CrowAgent_Logo_Horizontal_Dark.svg"

# Segment Definitions
SEGMENT_DEFINITIONS = {
    "Commercial Landlord": {
        "class": "CommercialLandlordSegment",
        "module": "app.segments.commercial_landlord"
    },
    "SMB Industrial": {
        "class": "SMBIndustrialSegment",
        "module": "app.segments.smb_industrial"
    },
    "University/HE": {
        "class": "UniversityHESegment",
        "module": "app.segments.university_he"
    }
}
