from typing import TypedDict

class SensorDescription(TypedDict):
    icon: Union[str, None]
    label: str
    unit: Union[str, None]
    enabled: bool
    state_class: Union[str, None]
    device_class: Union[str, None]
