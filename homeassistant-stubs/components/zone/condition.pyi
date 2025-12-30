import voluptuous as vol
from . import in_zone as in_zone
from _typeshed import Incomplete
from homeassistant.const import ATTR_GPS_ACCURACY as ATTR_GPS_ACCURACY, ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_OPTIONS as CONF_OPTIONS, CONF_ZONE as CONF_ZONE, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.exceptions import ConditionErrorContainer as ConditionErrorContainer, ConditionErrorMessage as ConditionErrorMessage
from homeassistant.helpers.automation import move_top_level_schema_fields_to_options as move_top_level_schema_fields_to_options
from homeassistant.helpers.condition import Condition as Condition, ConditionCheckParams as ConditionCheckParams, ConditionChecker as ConditionChecker, ConditionConfig as ConditionConfig
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_OPTIONS_SCHEMA_DICT: dict[vol.Marker, Any]
_CONDITION_SCHEMA: Incomplete

def zone(hass: HomeAssistant, zone_ent: str | State | None, entity: str | State | None) -> bool: ...

class ZoneCondition(Condition):
    _options: dict[str, Any]
    @classmethod
    async def async_validate_complete_config(cls, hass: HomeAssistant, complete_config: ConfigType) -> ConfigType: ...
    @classmethod
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    def __init__(self, hass: HomeAssistant, config: ConditionConfig) -> None: ...
    async def async_get_checker(self) -> ConditionChecker: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
