from dataclasses import dataclass
from datetime import datetime
from here_routing import RoutingMode as RoutingMode, TrafficMode as TrafficMode
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
    route_mode: RoutingMode
    arrival: datetime | None
    departure: datetime | None
    traffic_mode: TrafficMode
