from _typeshed import Incomplete
from collections.abc import Mapping
from functools import cache
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorStateClass as SensorStateClass
from typing import TypedDict
from xknx.dpt import DPTBase

HaDptClass: Incomplete

class DPTInfo(TypedDict):
    dpt_class: HaDptClass
    main: int
    sub: int | None
    name: str | None
    unit: str | None
    sensor_device_class: SensorDeviceClass | None
    sensor_state_class: SensorStateClass | None

@cache
def get_supported_dpts() -> Mapping[str, DPTInfo]: ...
def _ha_dpt_class(dpt_cls: type[DPTBase]) -> HaDptClass: ...

_sensor_device_classes: Mapping[str, SensorDeviceClass]
_sensor_state_class_overrides: Mapping[str, SensorStateClass | None]

def _get_sensor_state_class(ha_dpt_class: HaDptClass, dpt_number_str: str) -> SensorStateClass | None: ...
