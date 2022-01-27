from ..const import DOMAIN as DOMAIN
from ..helpers import async_get_client_wrapper_by_device_entry as async_get_client_wrapper_by_device_entry, async_get_device_entry_by_device_id as async_get_device_entry_by_device_id, async_get_device_id_from_entity_id as async_get_device_id_from_entity_id
from homeassistant.components.automation import AutomationActionType as AutomationActionType, AutomationTriggerInfo as AutomationTriggerInfo
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

PLATFORM_TYPE: Any
TRIGGER_TYPE_TURN_ON: str
TRIGGER_SCHEMA: Any

async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: AutomationActionType, automation_info: AutomationTriggerInfo, *, platform_type: str = ...) -> Union[CALLBACK_TYPE, None]: ...
