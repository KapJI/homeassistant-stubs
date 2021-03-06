import voluptuous as vol
from . import DOMAIN as DOMAIN
from homeassistant.components.automation import AutomationActionType as AutomationActionType
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA
from homeassistant.components.homeassistant.triggers.state import CONF_FOR as CONF_FOR, CONF_FROM as CONF_FROM, CONF_TO as CONF_TO
from homeassistant.components.select.const import ATTR_OPTIONS as ATTR_OPTIONS
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.entity import get_capability as get_capability
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

TRIGGER_TYPES: Any
TRIGGER_SCHEMA: Any

async def async_get_triggers(hass: HomeAssistant, device_id: str) -> list[dict[str, Any]]: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: AutomationActionType, automation_info: dict) -> CALLBACK_TYPE: ...
async def async_get_trigger_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
