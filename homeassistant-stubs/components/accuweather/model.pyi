from typing import TypedDict

class SensorDescription(TypedDict):
    device_class: Union[str, None]
    icon: Union[str, None]
    label: str
    unit_metric: Union[str, None]
    unit_imperial: Union[str, None]
    enabled: bool
    state_class: Union[str, None]
