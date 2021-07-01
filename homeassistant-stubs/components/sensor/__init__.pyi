from collections.abc import Mapping
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_CO as DEVICE_CLASS_CO, DEVICE_CLASS_CO2 as DEVICE_CLASS_CO2, DEVICE_CLASS_CURRENT as DEVICE_CLASS_CURRENT, DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_ILLUMINANCE as DEVICE_CLASS_ILLUMINANCE, DEVICE_CLASS_MONETARY as DEVICE_CLASS_MONETARY, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, DEVICE_CLASS_POWER_FACTOR as DEVICE_CLASS_POWER_FACTOR, DEVICE_CLASS_PRESSURE as DEVICE_CLASS_PRESSURE, DEVICE_CLASS_SIGNAL_STRENGTH as DEVICE_CLASS_SIGNAL_STRENGTH, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP, DEVICE_CLASS_VOLTAGE as DEVICE_CLASS_VOLTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Final

_LOGGER: Final[Any]
ATTR_LAST_RESET: Final[str]
ATTR_STATE_CLASS: Final[str]
DOMAIN: Final[str]
ENTITY_ID_FORMAT: Final[Any]
SCAN_INTERVAL: Final[Any]
DEVICE_CLASSES: Final[list[str]]
DEVICE_CLASSES_SCHEMA: Final[Any]
STATE_CLASS_MEASUREMENT: Final[str]
STATE_CLASSES: Final[list[str]]
STATE_CLASSES_SCHEMA: Final[Any]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class SensorEntity(Entity):
    _attr_state_class: Union[str, None]
    _attr_last_reset: Union[datetime, None]
    @property
    def state_class(self) -> Union[str, None]: ...
    @property
    def last_reset(self) -> Union[datetime, None]: ...
    @property
    def capability_attributes(self) -> Union[Mapping[str, Any], None]: ...
    @property
    def state_attributes(self) -> Union[dict[str, Any], None]: ...
