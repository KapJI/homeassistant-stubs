from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.const import CONF_CONDITION as CONF_CONDITION, SUN_EVENT_SUNRISE as SUN_EVENT_SUNRISE, SUN_EVENT_SUNSET as SUN_EVENT_SUNSET
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.condition import Condition as Condition, ConditionCheckerType as ConditionCheckerType, condition_trace_set_result as condition_trace_set_result, condition_trace_update_result as condition_trace_update_result, trace_condition_function as trace_condition_function
from homeassistant.helpers.sun import get_astral_event_date as get_astral_event_date
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType

_CONDITION_SCHEMA: Incomplete

def sun(hass: HomeAssistant, before: str | None = None, after: str | None = None, before_offset: timedelta | None = None, after_offset: timedelta | None = None) -> bool: ...

class SunCondition(Condition):
    _config: Incomplete
    _hass: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConfigType) -> None: ...
    @classmethod
    async def async_validate_condition_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    async def async_condition_from_config(self) -> ConditionCheckerType: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
