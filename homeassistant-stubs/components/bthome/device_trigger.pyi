from .const import BTHOME_BLE_EVENT as BTHOME_BLE_EVENT, CONF_DISCOVERED_EVENT_CLASSES as CONF_DISCOVERED_EVENT_CLASSES, CONF_SUBTYPE as CONF_SUBTYPE, DOMAIN as DOMAIN, EVENT_CLASS as EVENT_CLASS, EVENT_CLASS_BUTTON as EVENT_CLASS_BUTTON, EVENT_CLASS_DIMMER as EVENT_CLASS_DIMMER, EVENT_TYPE as EVENT_TYPE
from _typeshed import Incomplete
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_EVENT as CONF_EVENT, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

TRIGGERS_BY_EVENT_CLASS: Incomplete
SCHEMA_BY_EVENT_CLASS: Incomplete

async def async_validate_trigger_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_get_triggers(hass: HomeAssistant, device_id: str) -> list[dict[str, Any]]: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
