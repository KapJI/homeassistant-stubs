import abc
import voluptuous as vol
from . import in_zone as in_zone
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.device_tracker import ATTR_IN_ZONES as ATTR_IN_ZONES
from homeassistant.const import ATTR_GPS_ACCURACY as ATTR_GPS_ACCURACY, ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_FOR as CONF_FOR, CONF_OPTIONS as CONF_OPTIONS, CONF_TARGET as CONF_TARGET, CONF_ZONE as CONF_ZONE, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.exceptions import ConditionErrorContainer as ConditionErrorContainer, ConditionErrorMessage as ConditionErrorMessage
from homeassistant.helpers.automation import DomainSpec as DomainSpec, move_top_level_schema_fields_to_options as move_top_level_schema_fields_to_options
from homeassistant.helpers.condition import ATTR_BEHAVIOR as ATTR_BEHAVIOR, BEHAVIOR_ANY as BEHAVIOR_ANY, Condition as Condition, ConditionCheckParams as ConditionCheckParams, ConditionConfig as ConditionConfig, ENTITY_STATE_CONDITION_SCHEMA_ANY_ALL as ENTITY_STATE_CONDITION_SCHEMA_ANY_ALL, EntityConditionBase as EntityConditionBase
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Unpack

_OPTIONS_SCHEMA_DICT: dict[vol.Marker, Any]
_CONDITION_SCHEMA: Incomplete

def zone(hass: HomeAssistant, zone_ent: str | State | None, entity: str | State | None) -> bool: ...

class ZoneCondition(Condition):
    _options: dict[str, Any]
    @classmethod
    async def async_validate_complete_config(cls, hass: HomeAssistant, complete_config: ConfigType) -> ConfigType: ...
    @classmethod
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    _entity_ids: Incomplete
    _zone_entity_ids: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConditionConfig) -> None: ...
    def _async_check(self, **kwargs: Unpack[ConditionCheckParams]) -> bool: ...

_DOMAIN_SPECS: dict[str, DomainSpec]
_ZONE_CONDITION_SCHEMA: Incomplete

class _ZoneTargetConditionBase(EntityConditionBase, metaclass=abc.ABCMeta):
    _domain_specs = _DOMAIN_SPECS
    _schema = _ZONE_CONDITION_SCHEMA
    _zone: str
    def __init__(self, hass: HomeAssistant, config: ConditionConfig) -> None: ...
    def _in_target_zone(self, entity_state: State) -> bool: ...

class InZoneCondition(_ZoneTargetConditionBase):
    def is_valid_state(self, entity_state: State) -> bool: ...

class NotInZoneCondition(_ZoneTargetConditionBase):
    def is_valid_state(self, entity_state: State) -> bool: ...

_OCCUPANCY_CONDITION_SCHEMA: Incomplete

class _ZoneOccupancyConditionBase(EntityConditionBase, metaclass=abc.ABCMeta):
    _domain_specs: Incomplete
    _schema = _OCCUPANCY_CONDITION_SCHEMA
    @classmethod
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    @staticmethod
    def _occupancy_count(entity_state: State) -> int | None: ...
    @classmethod
    def _is_occupied(cls, entity_state: State) -> bool: ...

class OccupancyIsDetectedCondition(_ZoneOccupancyConditionBase):
    def is_valid_state(self, entity_state: State) -> bool: ...

class OccupancyIsNotDetectedCondition(_ZoneOccupancyConditionBase):
    def is_valid_state(self, entity_state: State) -> bool: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
