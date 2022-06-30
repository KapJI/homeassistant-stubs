from canary.model import Location as Location
from collections.abc import ValuesView
from typing import Optional, TypedDict

class CanaryData(TypedDict):
    locations: dict[str, Location]
    readings: dict[str, ValuesView]
SensorTypeItem = tuple[str, Optional[str], Optional[str], Optional[str], list[str]]
