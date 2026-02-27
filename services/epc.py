"""EPC data service integration layer.

Provides a production-safe accessor for EPC-like building metadata with a
network-backed path (when configured) and a deterministic stub fallback.
"""

from __future__ import annotations

import os
from typing import Any

import requests



EPC_API_URL_ENV = "EPC_API_URL"
EPC_API_KEY_ENV = "EPC_API_KEY"


def fetch_epc_data(postcode: str, timeout_s: int = 10) -> dict[str, Any]:
    """Fetch EPC-like data for a UK postcode.

    The function attempts a real API call if ``EPC_API_URL`` is configured,
    otherwise returns a deterministic stub payload suitable for local/dev use.

    Args:
        postcode: UK postcode string.
        timeout_s: HTTP timeout in seconds for upstream API requests.

    Returns:
        JSON-like dict with keys ``floor_area_m2``, ``built_year``, ``epc_band``.

    Raises:
        ValueError: If postcode format is invalid.
    """
    normalized = " ".join(postcode.strip().upper().split())
    if len(normalized) < 5:
        raise ValueError("Invalid postcode format.")

    api_url = os.getenv(EPC_API_URL_ENV, "").strip()
    api_key = os.getenv(EPC_API_KEY_ENV, "").strip()

    if api_url:
        headers = {"Accept": "application/json"}
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"
        try:
            resp = requests.get(
                api_url,
                params={"postcode": normalized},
                headers=headers,
                timeout=timeout_s,
            )
            resp.raise_for_status()
            payload = resp.json() if resp.content else {}
            return {
                "floor_area_m2": float(payload.get("floor_area_m2", 450.0)),
                "built_year": int(payload.get("built_year", 1995)),
                "epc_band": str(payload.get("epc_band", "D")),
                "_is_stub": False,
                "_stub_reason": "",
            }
        except Exception:
            # Fall through to deterministic stub for resilience.
            # _is_stub=True lets callers display a transparency warning (DEF-008).
            return {
                "floor_area_m2": 450.0,
                "built_year": 1995,
                "epc_band": "D",
                "_is_stub": True,
                "_stub_reason": "EPC API request failed; using deterministic estimate.",
            }

    return {
        "floor_area_m2": 450.0,
        "built_year": 1995,
        "epc_band": "D",
        "_is_stub": True,
        "_stub_reason": "EPC API not configured; using deterministic estimate.",
    }


def search_addresses(query: str, limit: int = 5, timeout_s: int = 8) -> list[dict[str, Any]]:
    """Search UK addresses for picker UX using Nominatim (fallback-safe)."""
    q = query.strip()
    if len(q) < 3:
        return []
    try:
        resp = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={"q": q, "countrycodes": "gb", "format": "jsonv2", "addressdetails": 1, "limit": limit},
            headers={"User-Agent": "CrowAgentPlatform/2.0"},
            timeout=timeout_s,
        )
        resp.raise_for_status()
        rows = resp.json() if resp.content else []
    except Exception:
        return []

    out: list[dict[str, Any]] = []
    for row in rows:
        disp = str(row.get("display_name", "")).strip()
        if not disp:
            continue
        out.append({
            "label": disp,
            "lat": float(row.get("lat", 0.0) or 0.0),
            "lon": float(row.get("lon", 0.0) or 0.0),
            "postcode": str((row.get("address") or {}).get("postcode", "")).upper().strip(),
        })
    return out
