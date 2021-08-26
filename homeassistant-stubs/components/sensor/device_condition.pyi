from . import DOMAIN as DOMAIN
from homeassistant.components.device_automation.exceptions import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from homeassistant.const import CONF_ABOVE as CONF_ABOVE, CONF_BELOW as CONF_BELOW, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_CO as DEVICE_CLASS_CO, DEVICE_CLASS_CO2 as DEVICE_CLASS_CO2, DEVICE_CLASS_CURRENT as DEVICE_CLASS_CURRENT, DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_GAS as DEVICE_CLASS_GAS, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_ILLUMINANCE as DEVICE_CLASS_ILLUMINANCE, DEVICE_CLASS_NITROGEN_DIOXIDE as DEVICE_CLASS_NITROGEN_DIOXIDE, DEVICE_CLASS_NITROGEN_MONOXIDE as DEVICE_CLASS_NITROGEN_MONOXIDE, DEVICE_CLASS_NITROUS_OXIDE as DEVICE_CLASS_NITROUS_OXIDE, DEVICE_CLASS_OZONE as DEVICE_CLASS_OZONE, DEVICE_CLASS_PM1 as DEVICE_CLASS_PM1, DEVICE_CLASS_PM10 as DEVICE_CLASS_PM10, DEVICE_CLASS_PM25 as DEVICE_CLASS_PM25, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, DEVICE_CLASS_POWER_FACTOR as DEVICE_CLASS_POWER_FACTOR, DEVICE_CLASS_PRESSURE as DEVICE_CLASS_PRESSURE, DEVICE_CLASS_SIGNAL_STRENGTH as DEVICE_CLASS_SIGNAL_STRENGTH, DEVICE_CLASS_SULPHUR_DIOXIDE as DEVICE_CLASS_SULPHUR_DIOXIDE, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_VOLATILE_ORGANIC_COMPOUNDS as DEVICE_CLASS_VOLATILE_ORGANIC_COMPOUNDS, DEVICE_CLASS_VOLTAGE as DEVICE_CLASS_VOLTAGE
from homeassistant.core import HomeAssistant as HomeAssistant, HomeAssistantError as HomeAssistantError, callback as callback
from homeassistant.helpers import condition as condition
from homeassistant.helpers.entity import get_device_class as get_device_class, get_unit_of_measurement as get_unit_of_measurement
from homeassistant.helpers.entity_registry import async_entries_for_device as async_entries_for_device, async_get_registry as async_get_registry
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

DEVICE_CLASS_NONE: str
CONF_IS_BATTERY_LEVEL: str
CONF_IS_CO: str
CONF_IS_CO2: str
CONF_IS_CURRENT: str
CONF_IS_ENERGY: str
CONF_IS_HUMIDITY: str
CONF_IS_GAS: str
CONF_IS_ILLUMINANCE: str
CONF_IS_NITROGEN_DIOXIDE: str
CONF_IS_NITROGEN_MONOXIDE: str
CONF_IS_NITROUS_OXIDE: str
CONF_IS_OZONE: str
CONF_IS_PM1: str
CONF_IS_PM10: str
CONF_IS_PM25: str
CONF_IS_POWER: str
CONF_IS_POWER_FACTOR: str
CONF_IS_PRESSURE: str
CONF_IS_SIGNAL_STRENGTH: str
CONF_IS_SULPHUR_DIOXIDE: str
CONF_IS_TEMPERATURE: str
CONF_IS_VOLATILE_ORGANIC_COMPOUNDS: str
CONF_IS_VOLTAGE: str
CONF_IS_VALUE: str
ENTITY_CONDITIONS: Any
CONDITION_SCHEMA: Any

async def async_get_conditions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
def async_condition_from_config(config: ConfigType, config_validation: bool) -> condition.ConditionCheckerType: ...
async def async_get_condition_capabilities(hass, config): ...
