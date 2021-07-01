from typing import Callable, TypedDict

class SensorDescription(TypedDict):
    device_class: Union[str, None]
    icon: Union[str, None]
    label: str
    unit: str
    state_class: Union[str, None]
    value: Callable
