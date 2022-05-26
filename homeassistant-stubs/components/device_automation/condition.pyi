import abc
import voluptuous as vol
from . import DeviceAutomationType as DeviceAutomationType, async_get_device_automation_platform as async_get_device_automation_platform
from .exceptions import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from collections.abc import Awaitable
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import condition as condition
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

class DeviceAutomationConditionProtocol(metaclass=abc.ABCMeta):
    CONDITION_SCHEMA: vol.Schema
    async def async_validate_condition_config(self, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    def async_condition_from_config(self, hass: HomeAssistant, config: ConfigType) -> condition.ConditionCheckerType: ...
    def async_get_condition_capabilities(self, hass: HomeAssistant, config: ConfigType) -> Union[dict[str, vol.Schema], Awaitable[dict[str, vol.Schema]]]: ...
    def async_get_conditions(self, hass: HomeAssistant, device_id: str) -> Union[list[dict[str, Any]], Awaitable[list[dict[str, Any]]]]: ...

async def async_validate_condition_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_condition_from_config(hass: HomeAssistant, config: ConfigType) -> condition.ConditionCheckerType: ...
