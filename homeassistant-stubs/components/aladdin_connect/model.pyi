from typing import TypedDict

class DoorDevice(TypedDict):
    device_id: str
    door_number: int
    name: str
    status: str
    serial: str
    model: str
