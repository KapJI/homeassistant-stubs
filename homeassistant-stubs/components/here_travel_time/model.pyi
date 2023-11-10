from dataclasses import dataclass
from datetime import time
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
class HERETravelTimeConfig:
    destination_latitude: float | None
    destination_longitude: float | None
    destination_entity_id: str | None
    origin_latitude: float | None
    origin_longitude: float | None
    origin_entity_id: str | None
    travel_mode: str
    route_mode: str
    arrival: time | None
    departure: time | None
    def __init__(self, destination_latitude, destination_longitude, destination_entity_id, origin_latitude, origin_longitude, origin_entity_id, travel_mode, route_mode, arrival, departure) -> None: ...
