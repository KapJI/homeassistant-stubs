import abc
import voluptuous as vol
from . import DeviceAutomationType as DeviceAutomationType, async_get_device_automation_platform as async_get_device_automation_platform
from .exceptions import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

class DeviceAutomationActionProtocol(metaclass=abc.ABCMeta):
    ACTION_SCHEMA: vol.Schema
    async def async_validate_action_config(self, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    async def async_call_action_from_config(self, hass: HomeAssistant, config: ConfigType, variables: dict[str, Any], context: Union[Context, None]) -> None: ...

async def async_validate_action_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_call_action_from_config(hass: HomeAssistant, config: ConfigType, variables: dict[str, Any], context: Union[Context, None]) -> None: ...
