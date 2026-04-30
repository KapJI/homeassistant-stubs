import voluptuous as vol
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.const import CONF_OPTIONS as CONF_OPTIONS, SUN_EVENT_SUNRISE as SUN_EVENT_SUNRISE, SUN_EVENT_SUNSET as SUN_EVENT_SUNSET
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.automation import move_top_level_schema_fields_to_options as move_top_level_schema_fields_to_options
from homeassistant.helpers.condition import Condition as Condition, ConditionCheckParams as ConditionCheckParams, ConditionConfig as ConditionConfig, condition_trace_set_result as condition_trace_set_result, condition_trace_update_result as condition_trace_update_result
from homeassistant.helpers.sun import get_astral_event_date as get_astral_event_date
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Unpack

_OPTIONS_SCHEMA_DICT: dict[vol.Marker, Any]
_CONDITION_SCHEMA: Incomplete

def sun(hass: HomeAssistant, before: str | None = None, after: str | None = None, before_offset: timedelta | None = None, after_offset: timedelta | None = None) -> bool: ...

class SunCondition(Condition):
    _options: dict[str, Any]
    @classmethod
    async def async_validate_complete_config(cls, hass: HomeAssistant, complete_config: ConfigType) -> ConfigType: ...
    @classmethod
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    _before: Incomplete
    _after: Incomplete
    _before_offset: Incomplete
    _after_offset: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConditionConfig) -> None: ...
    def _async_check(self, **kwargs: Unpack[ConditionCheckParams]) -> bool: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
