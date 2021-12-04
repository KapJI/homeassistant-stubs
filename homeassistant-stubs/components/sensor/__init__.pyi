from .const import CONF_STATE_CLASS as CONF_STATE_CLASS
from collections.abc import Mapping
from datetime import date, datetime
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_AQI as DEVICE_CLASS_AQI, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_CO as DEVICE_CLASS_CO, DEVICE_CLASS_CO2 as DEVICE_CLASS_CO2, DEVICE_CLASS_CURRENT as DEVICE_CLASS_CURRENT, DEVICE_CLASS_DATE as DEVICE_CLASS_DATE, DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_FREQUENCY as DEVICE_CLASS_FREQUENCY, DEVICE_CLASS_GAS as DEVICE_CLASS_GAS, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_ILLUMINANCE as DEVICE_CLASS_ILLUMINANCE, DEVICE_CLASS_MONETARY as DEVICE_CLASS_MONETARY, DEVICE_CLASS_NITROGEN_DIOXIDE as DEVICE_CLASS_NITROGEN_DIOXIDE, DEVICE_CLASS_NITROGEN_MONOXIDE as DEVICE_CLASS_NITROGEN_MONOXIDE, DEVICE_CLASS_NITROUS_OXIDE as DEVICE_CLASS_NITROUS_OXIDE, DEVICE_CLASS_OZONE as DEVICE_CLASS_OZONE, DEVICE_CLASS_PM1 as DEVICE_CLASS_PM1, DEVICE_CLASS_PM10 as DEVICE_CLASS_PM10, DEVICE_CLASS_PM25 as DEVICE_CLASS_PM25, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, DEVICE_CLASS_POWER_FACTOR as DEVICE_CLASS_POWER_FACTOR, DEVICE_CLASS_PRESSURE as DEVICE_CLASS_PRESSURE, DEVICE_CLASS_SIGNAL_STRENGTH as DEVICE_CLASS_SIGNAL_STRENGTH, DEVICE_CLASS_SULPHUR_DIOXIDE as DEVICE_CLASS_SULPHUR_DIOXIDE, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP, DEVICE_CLASS_VOLATILE_ORGANIC_COMPOUNDS as DEVICE_CLASS_VOLATILE_ORGANIC_COMPOUNDS, DEVICE_CLASS_VOLTAGE as DEVICE_CLASS_VOLTAGE, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType, StateType as StateType
from typing import Any, Final

_LOGGER: Final[Any]
ATTR_LAST_RESET: Final[str]
ATTR_STATE_CLASS: Final[str]
DOMAIN: Final[str]
ENTITY_ID_FORMAT: Final[Any]
SCAN_INTERVAL: Final[Any]

class SensorDeviceClass(StrEnum):
    AQI: str
    BATTERY: str
    CO: str
    CO2: str
    CURRENT: str
    DATE: str
    ENERGY: str
    FREQUENCY: str
    GAS: str
    HUMIDITY: str
    ILLUMINANCE: str
    MONETARY: str
    NITROGEN_DIOXIDE: str
    NITROGEN_MONOXIDE: str
    NITROUS_OXIDE: str
    OZONE: str
    PM1: str
    PM10: str
    PM25: str
    POWER_FACTOR: str
    POWER: str
    PRESSURE: str
    SIGNAL_STRENGTH: str
    SULPHUR_DIOXIDE: str
    TEMPERATURE: str
    TIMESTAMP: str
    VOLATILE_ORGANIC_COMPOUNDS: str
    VOLTAGE: str

DEVICE_CLASSES_SCHEMA: Final[Any]
DEVICE_CLASSES: Final[list[str]]

class SensorStateClass(StrEnum):
    MEASUREMENT: str
    TOTAL: str
    TOTAL_INCREASING: str

STATE_CLASSES_SCHEMA: Final[Any]
STATE_CLASS_MEASUREMENT: Final[str]
STATE_CLASS_TOTAL: Final[str]
STATE_CLASS_TOTAL_INCREASING: Final[str]
STATE_CLASSES: Final[list[str]]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class SensorEntityDescription(EntityDescription):
    device_class: Union[SensorDeviceClass, str, None]
    last_reset: Union[datetime, None]
    native_unit_of_measurement: Union[str, None]
    state_class: Union[SensorStateClass, str, None]
    unit_of_measurement: None
    def __post_init__(self) -> None: ...

class SensorEntity(Entity):
    entity_description: SensorEntityDescription
    _attr_device_class: Union[SensorDeviceClass, str, None]
    _attr_last_reset: Union[datetime, None]
    _attr_native_unit_of_measurement: Union[str, None]
    _attr_native_value: Union[StateType, date, datetime]
    _attr_state_class: Union[SensorStateClass, str, None]
    _attr_state: None
    _attr_unit_of_measurement: None
    _last_reset_reported: bool
    _temperature_conversion_reported: bool
    __datetime_as_string_deprecation_logged: bool
    @property
    def device_class(self) -> Union[SensorDeviceClass, str, None]: ...
    @property
    def state_class(self) -> Union[SensorStateClass, str, None]: ...
    @property
    def last_reset(self) -> Union[datetime, None]: ...
    @property
    def capability_attributes(self) -> Union[Mapping[str, Any], None]: ...
    @property
    def state_attributes(self) -> Union[dict[str, Any], None]: ...
    @property
    def native_value(self) -> Union[StateType, date, datetime]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def state(self) -> Any: ...
    def __repr__(self) -> str: ...
