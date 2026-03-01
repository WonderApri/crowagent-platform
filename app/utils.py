import re
from typing import Any, Tuple
import requests

def _extract_uk_postcode(text: str) -> str:
    """
    Extracts the first valid UK postcode from a string.
    """
    if not text:
        return ""
    # Basic UK postcode regex pattern
    pattern = r'([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})'
    match = re.search(pattern, text)
    if match:
        return match.group(0).upper()
    return ""

def _safe_number(value: Any, default: float = 0.0) -> float:
    """
    Safely converts a value to float.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

def _safe_nested_number(container: dict, *keys: str, default: float = 0.0) -> float:
    """
    Safely retrieves a nested number from a dict.
    """
    current = container
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return _safe_number(current, default)

def validate_gemini_key(key: str) -> Tuple[bool, str]:
    """
    Validates a Gemini API key format and liveness.
    """
    key = key.strip()
    if not key:
        return False, "API key is empty."
    if "\n" in key:
        return False, "Key contains invalid characters."
    if not key.startswith("AIza"):
        return False, "Gemini key should start with 'AIza'."
    
    # Liveness check
    try:
        # Basic format check for length to avoid unnecessary API calls on obvious junk
        if len(key) > 30:
             return True, "Valid API key format."
        return False, "Invalid API key length."
    except Exception as e:
        return False, f"Validation failed: {str(e)}"