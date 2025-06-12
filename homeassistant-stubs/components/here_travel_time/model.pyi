from dataclasses import dataclass
from datetime import datetime
from typing import TypedDict

class HERETravelTimeData(TypedDict):
    attribution: str | None
    duration: float
    duration_in_traffic: float
    distance: float
    origin: str
    destination: str
    origin_name: str | None
    destination_name: str | None

@dataclass
class HERETravelTimeAPIParams:
    destination: list[str]
    origin: list[str]
    travel_mode: str
    route_mode: str
    arrival: datetime | None
    departure: datetime | None
