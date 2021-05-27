from canary.api import Location as Location
from collections.abc import ValuesView
from typing import List, Optional, Tuple, TypedDict

class CanaryData(TypedDict):
    locations: dict[str, Location]
    readings: dict[str, ValuesView]
SensorTypeItem = Tuple[str, Optional[str], Optional[str], Optional[str], List[str]]
