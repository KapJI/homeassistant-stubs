from _typeshed import Incomplete
from typing import TypedDict

class GarageDoorData(TypedDict):
    device_id: str
    door_number: int
    name: str
    status: str
    link_status: str
    battery_level: int

class GarageDoor:
    device_id: Incomplete
    door_number: Incomplete
    unique_id: Incomplete
    name: Incomplete
    status: Incomplete
    link_status: Incomplete
    battery_level: Incomplete
    def __init__(self, data: GarageDoorData) -> None: ...
