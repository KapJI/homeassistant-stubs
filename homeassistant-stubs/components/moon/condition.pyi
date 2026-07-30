import abc
from .const import CONF_PHASE as CONF_PHASE
from .helpers import MOON_PHASES as MOON_PHASES, is_waxing as is_waxing, moon_phase as moon_phase
from _typeshed import Incomplete
from homeassistant.const import CONF_OPTIONS as CONF_OPTIONS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.condition import Condition as Condition, ConditionCheckParams as ConditionCheckParams, ConditionConfig as ConditionConfig
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Unpack, override

_STATE_CONDITION_SCHEMA: Incomplete
_IS_PHASE_CONDITION_SCHEMA: Incomplete

class _MoonStateCondition(Condition, metaclass=abc.ABCMeta):
    @classmethod
    @override
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...

class _WaxingCondition(_MoonStateCondition):
    @override
    def _async_check(self, **kwargs: Unpack[ConditionCheckParams]) -> bool: ...

class _WaningCondition(_MoonStateCondition):
    @override
    def _async_check(self, **kwargs: Unpack[ConditionCheckParams]) -> bool: ...

class _IsPhaseCondition(Condition):
    @classmethod
    @override
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    _phase: str
    def __init__(self, hass: HomeAssistant, config: ConditionConfig) -> None: ...
    @override
    def _async_check(self, **kwargs: Unpack[ConditionCheckParams]) -> bool: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
