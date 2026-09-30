import probatio
from .const import NumberConf as NumberConf, PLATFORMS_WITHOUT_CONFIG_CATEGORY as PLATFORMS_WITHOUT_CONFIG_CATEGORY
from .dpt import DPTInfo as DPTInfo, get_supported_dpts as get_supported_dpts
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from enum import Enum
from homeassistant.components.sensor import DEVICE_CLASS_STATE_CLASSES as DEVICE_CLASS_STATE_CLASSES, DEVICE_CLASS_UNITS as DEVICE_CLASS_UNITS, STATE_CLASS_UNITS as STATE_CLASS_UNITS
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, EntityCategory as EntityCategory, Platform as Platform
from typing import Any
from xknx.dpt import DPTBase, DPTNumeric

_NUMBER_DEVICE_CLASS_UNITS: Incomplete
_SENSOR_DEVICE_CLASS_UNITS: Incomplete
_SENSOR_DEVICE_CLASS_STATE_CLASSES: Incomplete
_SENSOR_STATE_CLASS_UNITS: Incomplete

def dpt_subclass_validator(dpt_base_class: type[DPTBase]) -> Callable[[Any], str | int]: ...

dpt_base_type_validator: Incomplete
numeric_type_validator: Incomplete
string_type_validator: Incomplete
sensor_type_validator: Incomplete

def parse_entity_category(value: Any) -> EntityCategory | None: ...
def entity_category_supported(platform: Platform) -> Callable[[EntityCategory | None], EntityCategory | None]: ...
def entity_category_validator(platform: Platform) -> probatio.All: ...
def ga_validator(value: Any) -> str | int: ...
def maybe_ga_validator(value: Any) -> str | int | None: ...

ga_list_validator: Incomplete
ga_list_validator_optional: Incomplete
ia_validator: Incomplete

def ip_v4_validator(value: Any, multicast: bool | None = None) -> str: ...

sync_state_validator: Incomplete
sync_state_no_false_validator: Incomplete

def backwards_compatible_xknx_climate_enum_member(enumClass: type[Enum]) -> probatio.All: ...
def validate_number_attributes(transcoder: type[DPTNumeric], *, min_config: float | None, max_config: float | None, step_config: float | None, device_class: str | None, unit_of_measurement: str | None) -> None: ...
def validate_sensor_attributes(dpt_info: DPTInfo, *, state_class: str | None, device_class: str | None, unit_of_measurement: str | None) -> None: ...
