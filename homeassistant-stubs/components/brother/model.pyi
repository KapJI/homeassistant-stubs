from typing import TypedDict

class SensorDescription(TypedDict):
    icon: Union[str, None]
    label: str
    unit: Union[str, None]
    enabled: bool
