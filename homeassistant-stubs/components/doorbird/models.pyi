from .device import ConfiguredDoorBird as ConfiguredDoorBird
from dataclasses import dataclass
from typing import Any

@dataclass
class DoorBirdData:
    door_station: ConfiguredDoorBird
    door_station_info: dict[str, Any]
    event_entity_ids: dict[str, str]
    def __init__(self, door_station, door_station_info, event_entity_ids) -> None: ...
