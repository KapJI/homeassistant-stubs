from typing import TypedDict

class SensorDescription(TypedDict):
    label: str
    unit: Union[str, None]
    device_class: Union[str, None]
    icon: Union[str, None]
    enabled: bool
    state_class: Union[str, None]
