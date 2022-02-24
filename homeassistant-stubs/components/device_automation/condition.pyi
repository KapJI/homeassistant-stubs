import abc
import voluptuous as vol
from . import DeviceAutomationType as DeviceAutomationType, async_get_device_automation_platform as async_get_device_automation_platform
from .exceptions import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import condition as condition
from homeassistant.helpers.typing import ConfigType as ConfigType

class DeviceAutomationConditionProtocol(metaclass=abc.ABCMeta):
    CONDITION_SCHEMA: vol.Schema
    async def async_validate_condition_config(self, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    def async_condition_from_config(self, hass: HomeAssistant, config: ConfigType) -> condition.ConditionCheckerType: ...

async def async_validate_condition_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_condition_from_config(hass: HomeAssistant, config: ConfigType) -> condition.ConditionCheckerType: ...
