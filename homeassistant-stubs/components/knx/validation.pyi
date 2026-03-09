import voluptuous as vol
from .const import NumberConf as NumberConf
from .dpt import DPTInfo as DPTInfo, get_supported_dpts as get_supported_dpts
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from enum import Enum
from homeassistant.components.sensor import DEVICE_CLASS_STATE_CLASSES as DEVICE_CLASS_STATE_CLASSES, DEVICE_CLASS_UNITS as DEVICE_CLASS_UNITS, STATE_CLASS_UNITS as STATE_CLASS_UNITS
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from typing import Any
from xknx.dpt import DPTBase, DPTNumeric

def dpt_subclass_validator(dpt_base_class: type[DPTBase]) -> Callable[[Any], str | int]: ...

dpt_base_type_validator: Incomplete
numeric_type_validator: Incomplete
string_type_validator: Incomplete
sensor_type_validator: Incomplete

def ga_validator(value: Any) -> str | int: ...
def maybe_ga_validator(value: Any) -> str | int | None: ...

ga_list_validator: Incomplete
ga_list_validator_optional: Incomplete
ia_validator: Incomplete

def ip_v4_validator(value: Any, multicast: bool | None = None) -> str: ...

sync_state_validator: Incomplete

def backwards_compatible_xknx_climate_enum_member(enumClass: type[Enum]) -> vol.All: ...
def validate_number_attributes(transcoder: type[DPTNumeric], config: dict[str, Any]) -> dict[str, Any]: ...
def validate_sensor_attributes(dpt_info: DPTInfo, config: dict[str, Any]) -> dict[str, Any]: ...
