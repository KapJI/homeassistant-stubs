from . import DOMAIN as DOMAIN, SensorDeviceClass as SensorDeviceClass
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA
from homeassistant.components.device_automation.exceptions import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from homeassistant.const import CONF_ABOVE as CONF_ABOVE, CONF_BELOW as CONF_BELOW, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_FOR as CONF_FOR, CONF_TYPE as CONF_TYPE
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import get_device_class as get_device_class, get_unit_of_measurement as get_unit_of_measurement
from homeassistant.helpers.entity_registry import async_entries_for_device as async_entries_for_device
from typing import Any

DEVICE_CLASS_NONE: str
CONF_APPARENT_POWER: str
CONF_BATTERY_LEVEL: str
CONF_CO: str
CONF_CO2: str
CONF_CURRENT: str
CONF_ENERGY: str
CONF_FREQUENCY: str
CONF_GAS: str
CONF_HUMIDITY: str
CONF_ILLUMINANCE: str
CONF_NITROGEN_DIOXIDE: str
CONF_NITROGEN_MONOXIDE: str
CONF_NITROUS_OXIDE: str
CONF_OZONE: str
CONF_PM1: str
CONF_PM10: str
CONF_PM25: str
CONF_POWER: str
CONF_POWER_FACTOR: str
CONF_PRESSURE: str
CONF_REACTIVE_POWER: str
CONF_SIGNAL_STRENGTH: str
CONF_SULPHUR_DIOXIDE: str
CONF_TEMPERATURE: str
CONF_VOLATILE_ORGANIC_COMPOUNDS: str
CONF_VOLTAGE: str
CONF_VALUE: str
ENTITY_TRIGGERS: Any
TRIGGER_SCHEMA: Any

async def async_attach_trigger(hass, config, action, automation_info): ...
async def async_get_triggers(hass, device_id): ...
async def async_get_trigger_capabilities(hass, config): ...
