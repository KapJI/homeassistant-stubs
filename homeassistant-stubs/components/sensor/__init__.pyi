from .const import CONF_STATE_CLASS as CONF_STATE_CLASS
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from datetime import date, datetime
from decimal import Decimal
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, DEVICE_CLASS_AQI as DEVICE_CLASS_AQI, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_CO as DEVICE_CLASS_CO, DEVICE_CLASS_CO2 as DEVICE_CLASS_CO2, DEVICE_CLASS_CURRENT as DEVICE_CLASS_CURRENT, DEVICE_CLASS_DATE as DEVICE_CLASS_DATE, DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_FREQUENCY as DEVICE_CLASS_FREQUENCY, DEVICE_CLASS_GAS as DEVICE_CLASS_GAS, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_ILLUMINANCE as DEVICE_CLASS_ILLUMINANCE, DEVICE_CLASS_MONETARY as DEVICE_CLASS_MONETARY, DEVICE_CLASS_NITROGEN_DIOXIDE as DEVICE_CLASS_NITROGEN_DIOXIDE, DEVICE_CLASS_NITROGEN_MONOXIDE as DEVICE_CLASS_NITROGEN_MONOXIDE, DEVICE_CLASS_NITROUS_OXIDE as DEVICE_CLASS_NITROUS_OXIDE, DEVICE_CLASS_OZONE as DEVICE_CLASS_OZONE, DEVICE_CLASS_PM1 as DEVICE_CLASS_PM1, DEVICE_CLASS_PM10 as DEVICE_CLASS_PM10, DEVICE_CLASS_PM25 as DEVICE_CLASS_PM25, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, DEVICE_CLASS_POWER_FACTOR as DEVICE_CLASS_POWER_FACTOR, DEVICE_CLASS_PRESSURE as DEVICE_CLASS_PRESSURE, DEVICE_CLASS_SIGNAL_STRENGTH as DEVICE_CLASS_SIGNAL_STRENGTH, DEVICE_CLASS_SULPHUR_DIOXIDE as DEVICE_CLASS_SULPHUR_DIOXIDE, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP, DEVICE_CLASS_VOLATILE_ORGANIC_COMPOUNDS as DEVICE_CLASS_VOLATILE_ORGANIC_COMPOUNDS, DEVICE_CLASS_VOLTAGE as DEVICE_CLASS_VOLTAGE, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT, TEMP_KELVIN as TEMP_KELVIN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.restore_state import ExtraStoredData as ExtraStoredData, RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, StateType as StateType
from typing import Any, Final

_LOGGER: Final[Incomplete]
ATTR_LAST_RESET: Final[str]
ATTR_STATE_CLASS: Final[str]
DOMAIN: Final[str]
ENTITY_ID_FORMAT: Final[Incomplete]
SCAN_INTERVAL: Final[Incomplete]

class SensorDeviceClass(StrEnum):
    APPARENT_POWER: str
    AQI: str
    BATTERY: str
    CO: str
    CO2: str
    CURRENT: str
    DATE: str
    DURATION: str
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
    REACTIVE_POWER: str
    SIGNAL_STRENGTH: str
    SULPHUR_DIOXIDE: str
    TEMPERATURE: str
    TIMESTAMP: str
    VOLATILE_ORGANIC_COMPOUNDS: str
    VOLTAGE: str

DEVICE_CLASSES_SCHEMA: Final[Incomplete]
DEVICE_CLASSES: Final[list[str]]

class SensorStateClass(StrEnum):
    MEASUREMENT: str
    TOTAL: str
    TOTAL_INCREASING: str

STATE_CLASSES_SCHEMA: Final[Incomplete]
STATE_CLASS_MEASUREMENT: Final[str]
STATE_CLASS_TOTAL: Final[str]
STATE_CLASS_TOTAL_INCREASING: Final[str]
STATE_CLASSES: Final[list[str]]
UNIT_CONVERSIONS: dict[str, Callable[[float, str, str], float]]
UNIT_RATIOS: dict[str, dict[str, float]]
VALID_UNITS: dict[str, tuple[str, ...]]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class SensorEntityDescription(EntityDescription):
    device_class: Union[SensorDeviceClass, str, None]
    last_reset: Union[datetime, None]
    native_unit_of_measurement: Union[str, None]
    state_class: Union[SensorStateClass, str, None]
    unit_of_measurement: None
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

class SensorEntity(Entity):
    entity_description: SensorEntityDescription
    _attr_device_class: Union[SensorDeviceClass, str, None]
    _attr_last_reset: Union[datetime, None]
    _attr_native_unit_of_measurement: Union[str, None]
    _attr_native_value: Union[StateType, date, datetime, Decimal]
    _attr_state_class: Union[SensorStateClass, str, None]
    _attr_state: None
    _attr_unit_of_measurement: None
    _last_reset_reported: bool
    _temperature_conversion_reported: bool
    _sensor_option_unit_of_measurement: Union[str, None]
    __datetime_as_string_deprecation_logged: bool
    async def async_internal_added_to_hass(self) -> None: ...
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
    def native_value(self) -> Union[StateType, date, datetime, Decimal]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def state(self) -> Any: ...
    def __repr__(self) -> str: ...
    def async_registry_entry_updated(self) -> None: ...

class SensorExtraStoredData(ExtraStoredData):
    native_value: Union[StateType, date, datetime, Decimal]
    native_unit_of_measurement: Union[str, None]
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, restored: dict[str, Any]) -> Union[SensorExtraStoredData, None]: ...
    def __init__(self, native_value, native_unit_of_measurement) -> None: ...

class RestoreSensor(SensorEntity, RestoreEntity):
    @property
    def extra_restore_state_data(self) -> SensorExtraStoredData: ...
    async def async_get_last_sensor_data(self) -> Union[SensorExtraStoredData, None]: ...
