from . import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA, DeviceAutomationType as DeviceAutomationType, async_get_device_automation_platform as async_get_device_automation_platform
from .exceptions import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN
from typing import Any

TRIGGER_SCHEMA: Any

async def async_validate_trigger_config(hass, config): ...
async def async_attach_trigger(hass, config, action, automation_info): ...
