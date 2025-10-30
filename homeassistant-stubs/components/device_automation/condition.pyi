import voluptuous as vol
from . import DeviceAutomationType as DeviceAutomationType, async_get_device_automation_platform as async_get_device_automation_platform
from .helpers import async_validate_device_automation_config as async_validate_device_automation_config
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN, CONF_OPTIONS as CONF_OPTIONS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import condition as condition
from homeassistant.helpers.condition import Condition as Condition, ConditionCheckerType as ConditionCheckerType, ConditionConfig as ConditionConfig, trace_condition_function as trace_condition_function
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Protocol

class DeviceAutomationConditionProtocol(Protocol):
    CONDITION_SCHEMA: vol.Schema
    async def async_validate_condition_config(self, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    def async_condition_from_config(self, hass: HomeAssistant, config: ConfigType) -> ConditionCheckerType: ...
    async def async_get_condition_capabilities(self, hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
    async def async_get_conditions(self, hass: HomeAssistant, device_id: str) -> list[dict[str, Any]]: ...

class DeviceCondition(Condition):
    _hass: HomeAssistant
    _config: ConfigType
    @classmethod
    async def async_validate_complete_config(cls, hass: HomeAssistant, complete_config: ConfigType) -> ConfigType: ...
    @classmethod
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    def __init__(self, hass: HomeAssistant, config: ConditionConfig) -> None: ...
    async def async_get_checker(self) -> condition.ConditionCheckerType: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
