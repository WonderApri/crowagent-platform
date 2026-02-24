"""Zero-cost 3D/4D spatial visualisation module for CrowAgent Platform.

External services used (all free/open-source):

* OpenFreeMap tiles (liberty style) – CC-BY 4.0 (free, no token required).
* OpenStreetMap Overpass API – ODbL license (free, open data).
* Nominatim geocoding API – ODbL license (free, usage policy applies).

No Mapbox/Google/paid services are referenced.  All APIs above allow anonymous
access and impose rate limits only; usage in this module is zero cost.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

import math

import overpy
import pydeck as pdk
import requests
import streamlit as st
from plotly import graph_objects as go


def render_3d_energy_map(buildings_data: List[Dict[str, Any]]) -> None:
    """Render a 3D extrusion map of energy usage using :mod:`pydeck`.

    Parameters
    ----------
    buildings_data
        List of dictionaries containing keys ``name``, ``lat``, ``lon``,
        ``energy_kwh``, ``carbon_tonnes`` and ``scenario``.
    """
    if not buildings_data:
        st.info("No building data available to render.")
        return

    # compute carbon range for colour mapping
    carbons = [b["carbon_tonnes"] for b in buildings_data]
    min_c, max_c = min(carbons), max(carbons)
    def colour_for(c: float) -> List[int]:
        # linear interpolate between teal and red
        if max_c > min_c:
            frac = (c - min_c) / (max_c - min_c)
        else:
            frac = 0.0
        # teal -> red
        return [
            int(0 + frac * (220 - 0)),
            int(194 + frac * (50 - 194)),
            int(168 + frac * (50 - 168)),
        ]

    # create layer data
    layer = pdk.Layer(
        "ColumnLayer",
        data=[
            {
                "position": [b["lon"], b["lat"]],
                "height": b["energy_kwh"],
                "carbon": b["carbon_tonnes"],
                "name": b["name"],
                "scenario": b["scenario"],
            }
            for b in buildings_data
        ],
        get_position="position",
        get_elevation="height",
        elevation_scale=0.1,
        extruded=True,
        get_fill_color="[ 0, 194, 168 ]",  # placeholder, overridden by function below
        pickable=True,
        auto_highlight=True,
        get_fill_color=["carbon", "min_c", "max_c"],
        color_range=[[0, 194, 168], [220, 50, 50]],
    )

    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=pdk.ViewState(
            latitude=buildings_data[0]["lat"],
            longitude=buildings_data[0]["lon"],
            pitch=45,
            zoom=14,
        ),
        map_style="https://tiles.openfreemap.org/styles/liberty",
    )

    # legend HTML
    legend_html = (
        "<div style='font-size:0.8rem;color:#CBD8E6;'>"
        "<span style='background:#00C2A8;width:12px;height:12px;