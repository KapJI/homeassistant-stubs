from homeassistant.components.device_automation import TRIGGER_BASE_SCHEMA as TRIGGER_BASE_SCHEMA, async_get_device_automation_platform as async_get_device_automation_platform
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN
from typing import Any

TRIGGER_SCHEMA: Any

async def async_validate_trigger_config(hass: Any, config: Any): ...
async def async_attach_trigger(hass: Any, config: Any, action: Any, automation_info: Any): ...
