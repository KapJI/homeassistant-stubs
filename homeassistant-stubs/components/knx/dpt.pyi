from collections.abc import Mapping
from functools import cache
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfReactiveEnergy as UnitOfReactiveEnergy
from typing import Literal, NotRequired, TypedDict
from xknx.dpt import DPTBase, DPTComplex, DPTComplexFieldSchema as DPTComplexFieldSchema, DPTEnum, DPTNumeric

type HaDptClass = Literal['numeric', 'enum', 'complex', 'string']
class DPTInfo(TypedDict):
    dpt_class: HaDptClass
    main: int
    sub: int | None
    name: str | None
    unit: str | None
    sensor_device_class: SensorDeviceClass | None
    sensor_state_class: SensorStateClass | None
    payload_length: int
    min: NotRequired[float]
    max: NotRequired[float]
    step: NotRequired[float]
    options: NotRequired[list[str]]
    schema: NotRequired[list[DPTComplexFieldSchema]]

@cache
def get_supported_dpts() -> Mapping[str, DPTInfo]: ...
def _ha_dpt_class(dpt_cls: type[DPTBase]) -> HaDptClass: ...
def _add_numeric_details(dpt_info: DPTInfo, dpt_cls: type[DPTNumeric]) -> None: ...
def _add_enum_details(dpt_info: DPTInfo, dpt_cls: type[DPTEnum]) -> None: ...
def _add_complex_details(dpt_info: DPTInfo, dpt_cls: type[DPTComplex]) -> None: ...

_sensor_device_classes: Mapping[str, SensorDeviceClass]
_sensor_state_class_overrides: Mapping[str, SensorStateClass | None]
_sensor_unit_overrides: Mapping[str, str]

def _get_sensor_state_class(ha_dpt_class: HaDptClass, dpt_number_str: str) -> SensorStateClass | None: ...
