from .const import ATTR_MAX as ATTR_MAX, ATTR_MIN as ATTR_MIN, ATTR_STEP as ATTR_STEP, ATTR_VALUE as ATTR_VALUE, DEFAULT_MAX_VALUE as DEFAULT_MAX_VALUE, DEFAULT_MIN_VALUE as DEFAULT_MIN_VALUE, DEFAULT_STEP as DEFAULT_STEP, DOMAIN as DOMAIN, SERVICE_SET_VALUE as SERVICE_SET_VALUE
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_MODE as ATTR_MODE, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.restore_state import ExtraStoredData as ExtraStoredData, RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.unit_conversion import BaseUnitConverter as BaseUnitConverter, TemperatureConverter as TemperatureConverter
from typing import Any, Final

SCAN_INTERVAL: Incomplete
ENTITY_ID_FORMAT: Incomplete
MIN_TIME_BETWEEN_SCANS: Incomplete
_LOGGER: Incomplete

class NumberDeviceClass(StrEnum):
    APPARENT_POWER: str
    AQI: str
    BATTERY: str
    CO: str
    CO2: str
    CURRENT: str
    DISTANCE: str
    ENERGY: str
    FREQUENCY: str
    GAS: str
    HUMIDITY: str
    ILLUMINANCE: str
    MOISTURE: str
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
    PRECIPITATION: str
    PRECIPITATION_INTENSITY: str
    PRESSURE: str
    REACTIVE_POWER: str
    SIGNAL_STRENGTH: str
    SPEED: str
    SULPHUR_DIOXIDE: str
    TEMPERATURE: str
    VOLATILE_ORGANIC_COMPOUNDS: str
    VOLTAGE: str
    VOLUME: str
    WATER: str
    WEIGHT: str
    WIND_SPEED: str

DEVICE_CLASSES_SCHEMA: Final[Incomplete]

class NumberMode(StrEnum):
    AUTO: str
    BOX: str
    SLIDER: str

UNIT_CONVERTERS: dict[str, type[BaseUnitConverter]]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_set_value(entity: NumberEntity, service_call: ServiceCall) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class NumberEntityDescription(EntityDescription):
    max_value: None
    min_value: None
    native_max_value: Union[float, None]
    native_min_value: Union[float, None]
    native_unit_of_measurement: Union[str, None]
    native_step: Union[float, None]
    step: None
    unit_of_measurement: None
    def __post_init__(self) -> None: ...
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, max_value, min_value, native_max_value, native_min_value, native_unit_of_measurement, native_step, step) -> None: ...

def ceil_decimal(value: float, precision: float = ...) -> float: ...
def floor_decimal(value: float, precision: float = ...) -> float: ...

class NumberEntity(Entity):
    entity_description: NumberEntityDescription
    _attr_max_value: None
    _attr_min_value: None
    _attr_mode: NumberMode
    _attr_state: None
    _attr_step: None
    _attr_unit_of_measurement: None
    _attr_value: None
    _attr_native_max_value: float
    _attr_native_min_value: float
    _attr_native_step: float
    _attr_native_value: Union[float, None]
    _attr_native_unit_of_measurement: Union[str, None]
    _deprecated_number_entity_reported: bool
    _number_option_unit_of_measurement: Union[str, None]
    def __init_subclass__(cls, **kwargs: Any) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    @property
    def capability_attributes(self) -> dict[str, Any]: ...
    @property
    def native_min_value(self) -> float: ...
    @property
    def min_value(self) -> float: ...
    @property
    def native_max_value(self) -> float: ...
    @property
    def max_value(self) -> float: ...
    @property
    def native_step(self) -> Union[float, None]: ...
    @property
    def step(self) -> float: ...
    @property
    def mode(self) -> NumberMode: ...
    @property
    def state(self) -> Union[float, None]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def native_value(self) -> Union[float, None]: ...
    @property
    def value(self) -> Union[float, None]: ...
    def set_native_value(self, value: float) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
    def set_value(self, value: float) -> None: ...
    async def async_set_value(self, value: float) -> None: ...
    def _convert_to_state_value(self, value: float, method: Callable[[float, int], float]) -> float: ...
    def convert_to_native_value(self, value: float) -> float: ...
    def _report_deprecated_number_entity(self) -> None: ...
    def async_registry_entry_updated(self) -> None: ...

class NumberExtraStoredData(ExtraStoredData):
    native_max_value: Union[float, None]
    native_min_value: Union[float, None]
    native_step: Union[float, None]
    native_unit_of_measurement: Union[str, None]
    native_value: Union[float, None]
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, restored: dict[str, Any]) -> Union[NumberExtraStoredData, None]: ...
    def __init__(self, native_max_value, native_min_value, native_step, native_unit_of_measurement, native_value) -> None: ...

class RestoreNumber(NumberEntity, RestoreEntity):
    @property
    def extra_restore_state_data(self) -> NumberExtraStoredData: ...
    async def async_get_last_number_data(self) -> Union[NumberExtraStoredData, None]: ...
