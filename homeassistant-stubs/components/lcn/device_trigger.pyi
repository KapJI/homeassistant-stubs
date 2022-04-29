from .const import DOMAIN as DOMAIN, KEY_ACTIONS as KEY_ACTIONS, SENDKEYS as SENDKEYS
from _typeshed import Incomplete
from homeassistant.components.automation import AutomationActionType as AutomationActionType, AutomationTriggerInfo as AutomationTriggerInfo
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA
from homeassistant.components.homeassistant.triggers import event as event
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

TRIGGER_TYPES: Incomplete
LCN_DEVICE_TRIGGER_BASE_SCHEMA: Incomplete
ACCESS_CONTROL_SCHEMA: Incomplete
TRANSMITTER_SCHEMA: Incomplete
SENDKEYS_SCHEMA: Incomplete
TRIGGER_SCHEMA: Incomplete
TYPE_SCHEMAS: Incomplete

async def async_get_triggers(hass: HomeAssistant, device_id: str) -> list[dict[str, Any]]: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: AutomationActionType, automation_info: AutomationTriggerInfo) -> CALLBACK_TYPE: ...
async def async_get_trigger_capabilities(hass: HomeAssistant, config: dict) -> dict: ...
