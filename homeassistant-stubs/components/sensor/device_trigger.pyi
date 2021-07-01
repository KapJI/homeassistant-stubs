from . import DOMAIN as DOMAIN
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA
from homeassistant.components.device_automation.exceptions import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from homeassistant.const import CONF_ABOVE as CONF_ABOVE, CONF_BELOW as CONF_BELOW, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_FOR as CONF_FOR, CONF_TYPE as CONF_TYPE, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_CO as DEVICE_CLASS_CO, DEVICE_CLASS_CO2 as DEVICE_CLASS_CO2, DEVICE_CLASS_CURRENT as DEVICE_CLASS_CURRENT, DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_ILLUMINANCE as DEVICE_CLASS_ILLUMINANCE, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, DEVICE_CLASS_POWER_FACTOR as DEVICE_CLASS_POWER_FACTOR, DEVICE_CLASS_PRESSURE as DEVICE_CLASS_PRESSURE, DEVICE_CLASS_SIGNAL_STRENGTH as DEVICE_CLASS_SIGNAL_STRENGTH, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_VOLTAGE as DEVICE_CLASS_VOLTAGE
from homeassistant.core import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import get_device_class as get_device_class, get_unit_of_measurement as get_unit_of_measurement
from homeassistant.helpers.entity_registry import async_entries_for_device as async_entries_for_device
from typing import Any

DEVICE_CLASS_NONE: str
CONF_BATTERY_LEVEL: str
CONF_CO: str
CONF_CO2: str
CONF_CURRENT: str
CONF_ENERGY: str
CONF_HUMIDITY: str
CONF_ILLUMINANCE: str
CONF_POWER: str
CONF_POWER_FACTOR: str
CONF_PRESSURE: str
CONF_SIGNAL_STRENGTH: str
CONF_TEMPERATURE: str
CONF_VOLTAGE: str
CONF_VALUE: str
ENTITY_TRIGGERS: Any
TRIGGER_SCHEMA: Any

async def async_attach_trigger(hass, config, action, automation_info): ...
async def async_get_triggers(hass, device_id): ...
async def async_get_trigger_capabilities(hass, config): ...
