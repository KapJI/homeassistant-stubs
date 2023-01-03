from datetime import time
from typing import TypedDict

class HERETravelTimeData(TypedDict):
    attribution: Union[str, None]
    duration: float
    duration_in_traffic: float
    distance: float
    origin: str
    destination: str
    origin_name: Union[str, None]
    destination_name: Union[str, None]

class HERETravelTimeConfig:
    destination_latitude: Union[float, None]
    destination_longitude: Union[float, None]
    destination_entity_id: Union[str, None]
    origin_latitude: Union[float, None]
    origin_longitude: Union[float, None]
    origin_entity_id: Union[str, None]
    travel_mode: str
    route_mode: str
    arrival: Union[time, None]
    departure: Union[time, None]
    def __init__(self, destination_latitude, destination_longitude, destination_entity_id, origin_latitude, origin_longitude, origin_entity_id, travel_mode, route_mode, arrival, departure) -> None: ...
