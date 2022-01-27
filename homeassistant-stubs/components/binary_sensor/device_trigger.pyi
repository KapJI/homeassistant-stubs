from . import BinarySensorDeviceClass as BinarySensorDeviceClass, DOMAIN as DOMAIN
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA
from homeassistant.components.device_automation.const import CONF_TURNED_OFF as CONF_TURNED_OFF, CONF_TURNED_ON as CONF_TURNED_ON
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_FOR as CONF_FOR, CONF_TYPE as CONF_TYPE
from homeassistant.helpers.entity import get_device_class as get_device_class
from homeassistant.helpers.entity_registry import async_entries_for_device as async_entries_for_device
from typing import Any

DEVICE_CLASS_NONE: str
CONF_BAT_LOW: str
CONF_NOT_BAT_LOW: str
CONF_CHARGING: str
CONF_NOT_CHARGING: str
CONF_CO: str
CONF_NO_CO: str
CONF_COLD: str
CONF_NOT_COLD: str
CONF_CONNECTED: str
CONF_NOT_CONNECTED: str
CONF_GAS: str
CONF_NO_GAS: str
CONF_HOT: str
CONF_NOT_HOT: str
CONF_LIGHT: str
CONF_NO_LIGHT: str
CONF_LOCKED: str
CONF_NOT_LOCKED: str
CONF_MOIST: str
CONF_NOT_MOIST: str
CONF_MOTION: str
CONF_NO_MOTION: str
CONF_MOVING: str
CONF_NOT_MOVING: str
CONF_OCCUPIED: str
CONF_NOT_OCCUPIED: str
CONF_PLUGGED_IN: str
CONF_NOT_PLUGGED_IN: str
CONF_POWERED: str
CONF_NOT_POWERED: str
CONF_PRESENT: str
CONF_NOT_PRESENT: str
CONF_PROBLEM: str
CONF_NO_PROBLEM: str
CONF_RUNNING: str
CONF_NOT_RUNNING: str
CONF_UNSAFE: str
CONF_NOT_UNSAFE: str
CONF_SMOKE: str
CONF_NO_SMOKE: str
CONF_SOUND: str
CONF_NO_SOUND: str
CONF_TAMPERED: str
CONF_NOT_TAMPERED: str
CONF_UPDATE: str
CONF_NO_UPDATE: str
CONF_VIBRATION: str
CONF_NO_VIBRATION: str
CONF_OPENED: str
CONF_NOT_OPENED: str
TURNED_ON: Any
TURNED_OFF: Any
ENTITY_TRIGGERS: Any
TRIGGER_SCHEMA: Any

async def async_attach_trigger(hass, config, action, automation_info): ...
async def async_get_triggers(hass, device_id): ...
async def async_get_trigger_capabilities(hass, config): ...
