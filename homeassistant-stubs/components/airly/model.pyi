from typing import TypedDict

class SensorDescription(TypedDict):
    device_class: Union[str, None]
    icon: Union[str, None]
    label: str
    unit: str
