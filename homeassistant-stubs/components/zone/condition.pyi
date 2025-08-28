from . import in_zone as in_zone
from _typeshed import Incomplete
from homeassistant.const import ATTR_GPS_ACCURACY as ATTR_GPS_ACCURACY, ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_CONDITION as CONF_CONDITION, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_ZONE as CONF_ZONE, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.exceptions import ConditionErrorContainer as ConditionErrorContainer, ConditionErrorMessage as ConditionErrorMessage
from homeassistant.helpers.condition import Condition as Condition, ConditionCheckerType as ConditionCheckerType, trace_condition_function as trace_condition_function
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType

_CONDITION_SCHEMA: Incomplete

def zone(hass: HomeAssistant, zone_ent: str | State | None, entity: str | State | None) -> bool: ...

class ZoneCondition(Condition):
    _config: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConfigType) -> None: ...
    @classmethod
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    async def async_get_checker(self) -> ConditionCheckerType: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
