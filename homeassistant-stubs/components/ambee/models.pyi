from typing import TypedDict

class AmbeeSensor(TypedDict):
    device_class: str
    enabled_by_default: bool
    icon: str
    name: str
    state_class: str
    unit_of_measurement: str
