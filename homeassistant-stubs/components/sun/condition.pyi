from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.const import CONF_CONDITION as CONF_CONDITION, SUN_EVENT_SUNRISE as SUN_EVENT_SUNRISE, SUN_EVENT_SUNSET as SUN_EVENT_SUNSET
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.condition import ConditionCheckerType as ConditionCheckerType, condition_trace_set_result as condition_trace_set_result, condition_trace_update_result as condition_trace_update_result, trace_condition_function as trace_condition_function
from homeassistant.helpers.sun import get_astral_event_date as get_astral_event_date
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType

_CONDITION_SCHEMA: Incomplete

async def async_validate_condition_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
def sun(hass: HomeAssistant, before: str | None = None, after: str | None = None, before_offset: timedelta | None = None, after_offset: timedelta | None = None) -> bool: ...
def async_condition_from_config(config: ConfigType) -> ConditionCheckerType: ...
