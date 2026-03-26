import voluptuous as vol
from .entity import get_device_class_or_undefined as get_device_class_or_undefined
from .typing import ConfigType as ConfigType, UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from enum import Enum
from homeassistant.const import CONF_OPTIONS as CONF_OPTIONS
from homeassistant.core import HomeAssistant as HomeAssistant, split_entity_id as split_entity_id
from typing import Any, Final, Self

CONF_UNIT: Final[str]

class AnyDeviceClassType(Enum):
    _singleton = 0

ANY_DEVICE_CLASS: Incomplete

@dataclass(frozen=True, slots=True)
class DomainSpec:
    device_class: str | None | AnyDeviceClassType = ...
    value_source: str | None = ...

@dataclass(frozen=True, slots=True)
class NumericalDomainSpec(DomainSpec):
    value_converter: Callable[[float], float] | None = ...

def filter_by_domain_specs(hass: HomeAssistant, domain_specs: Mapping[str, DomainSpec], entities: set[str]) -> set[str]: ...
def get_absolute_description_key(domain: str, key: str) -> str: ...
def get_relative_description_key(domain: str, key: str) -> str: ...
def move_top_level_schema_fields_to_options(config: ConfigType, options_schema_dict: dict[vol.Marker, Any]) -> ConfigType: ...
def move_options_fields_to_top_level(config: ConfigType, base_schema: vol.Schema) -> ConfigType: ...

@dataclass(frozen=True, kw_only=True)
class ThresholdConfig:
    numerical: bool
    entity: str | None
    number: float | None
    unit: str | None | UndefinedType
    @classmethod
    def from_config(cls, config: dict[str, Any] | None) -> Self | None: ...
