import voluptuous as vol
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.const import CONF_OPTIONS as CONF_OPTIONS, CONF_TARGET as CONF_TARGET, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, split_entity_id as split_entity_id
from homeassistant.helpers import target as target
from homeassistant.helpers.condition import Condition as Condition, ConditionCheckerType as ConditionCheckerType, ConditionConfig as ConditionConfig, trace_condition_function as trace_condition_function
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from typing import Any, Final, override

ATTR_BEHAVIOR: Final[str]
BEHAVIOR_ANY: Final[str]
BEHAVIOR_ALL: Final[str]
STATE_CONDITION_VALID_STATES: Final[Incomplete]
STATE_CONDITION_OPTIONS_SCHEMA: dict[vol.Marker, Any]
STATE_CONDITION_SCHEMA: Incomplete

class StateConditionBase(Condition):
    @override
    @classmethod
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    _hass: Incomplete
    _target: Incomplete
    _behavior: Incomplete
    _state: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConditionConfig, state: str) -> None: ...
    @override
    async def async_get_checker(self) -> ConditionCheckerType: ...

class IsOnCondition(StateConditionBase):
    def __init__(self, hass: HomeAssistant, config: ConditionConfig) -> None: ...

class IsOffCondition(StateConditionBase):
    def __init__(self, hass: HomeAssistant, config: ConditionConfig) -> None: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
