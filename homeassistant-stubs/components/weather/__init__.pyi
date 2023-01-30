from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PRECISION_HALVES as PRECISION_HALVES, PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfLength as UnitOfLength, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.unit_conversion import DistanceConverter as DistanceConverter, PressureConverter as PressureConverter, SpeedConverter as SpeedConverter, TemperatureConverter as TemperatureConverter
from homeassistant.util.unit_system import US_CUSTOMARY_SYSTEM as US_CUSTOMARY_SYSTEM
from typing import Any, Final, TypedDict
from typing_extensions import Required

_LOGGER: Incomplete
ATTR_CONDITION_CLASS: str
ATTR_CONDITION_CLEAR_NIGHT: str
ATTR_CONDITION_CLOUDY: str
ATTR_CONDITION_EXCEPTIONAL: str
ATTR_CONDITION_FOG: str
ATTR_CONDITION_HAIL: str
ATTR_CONDITION_LIGHTNING: str
ATTR_CONDITION_LIGHTNING_RAINY: str
ATTR_CONDITION_PARTLYCLOUDY: str
ATTR_CONDITION_POURING: str
ATTR_CONDITION_RAINY: str
ATTR_CONDITION_SNOWY: str
ATTR_CONDITION_SNOWY_RAINY: str
ATTR_CONDITION_SUNNY: str
ATTR_CONDITION_WINDY: str
ATTR_CONDITION_WINDY_VARIANT: str
ATTR_FORECAST: str
ATTR_FORECAST_CONDITION: Final[str]
ATTR_FORECAST_NATIVE_PRECIPITATION: Final[str]
ATTR_FORECAST_PRECIPITATION: Final[str]
ATTR_FORECAST_PRECIPITATION_PROBABILITY: Final[str]
ATTR_FORECAST_NATIVE_PRESSURE: Final[str]
ATTR_FORECAST_PRESSURE: Final[str]
ATTR_FORECAST_NATIVE_TEMP: Final[str]
ATTR_FORECAST_TEMP: Final[str]
ATTR_FORECAST_NATIVE_TEMP_LOW: Final[str]
ATTR_FORECAST_TEMP_LOW: Final[str]
ATTR_FORECAST_TIME: Final[str]
ATTR_FORECAST_WIND_BEARING: Final[str]
ATTR_FORECAST_NATIVE_WIND_SPEED: Final[str]
ATTR_FORECAST_WIND_SPEED: Final[str]
ATTR_WEATHER_HUMIDITY: str
ATTR_WEATHER_OZONE: str
ATTR_WEATHER_PRESSURE: str
ATTR_WEATHER_PRESSURE_UNIT: str
ATTR_WEATHER_TEMPERATURE: str
ATTR_WEATHER_TEMPERATURE_UNIT: str
ATTR_WEATHER_VISIBILITY: str
ATTR_WEATHER_VISIBILITY_UNIT: str
ATTR_WEATHER_WIND_BEARING: str
ATTR_WEATHER_WIND_SPEED: str
ATTR_WEATHER_WIND_SPEED_UNIT: str
ATTR_WEATHER_PRECIPITATION_UNIT: str
DOMAIN: str
ENTITY_ID_FORMAT: Incomplete
SCAN_INTERVAL: Incomplete
ROUNDING_PRECISION: int
VALID_UNITS_PRESSURE: set[str]
VALID_UNITS_TEMPERATURE: set[str]
VALID_UNITS_PRECIPITATION: set[str]
VALID_UNITS_VISIBILITY: set[str]
VALID_UNITS_WIND_SPEED: set[str]
UNIT_CONVERSIONS: dict[str, Callable[[float, str, str], float]]
VALID_UNITS: dict[str, set[str]]

def round_temperature(temperature: Union[float, None], precision: float) -> Union[float, None]: ...

class Forecast(TypedDict):
    condition: Union[str, None]
    datetime: Required[str]
    precipitation_probability: Union[int, None]
    native_precipitation: Union[float, None]
    precipitation: None
    native_pressure: Union[float, None]
    pressure: None
    native_temperature: Union[float, None]
    temperature: None
    native_templow: Union[float, None]
    templow: None
    wind_bearing: Union[float, str, None]
    native_wind_speed: Union[float, None]
    wind_speed: None

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class WeatherEntityDescription(EntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class WeatherEntity(Entity):
    entity_description: WeatherEntityDescription
    _attr_condition: Union[str, None]
    _attr_forecast: Union[list[Forecast], None]
    _attr_humidity: Union[float, None]
    _attr_ozone: Union[float, None]
    _attr_precision: float
    _attr_pressure: None
    _attr_pressure_unit: None
    _attr_state: None
    _attr_temperature: None
    _attr_temperature_unit: None
    _attr_visibility: None
    _attr_visibility_unit: None
    _attr_precipitation_unit: None
    _attr_wind_bearing: Union[float, str, None]
    _attr_wind_speed: None
    _attr_wind_speed_unit: None
    _attr_native_pressure: Union[float, None]
    _attr_native_pressure_unit: Union[str, None]
    _attr_native_temperature: Union[float, None]
    _attr_native_temperature_unit: Union[str, None]
    _attr_native_visibility: Union[float, None]
    _attr_native_visibility_unit: Union[str, None]
    _attr_native_precipitation_unit: Union[str, None]
    _attr_native_wind_speed: Union[float, None]
    _attr_native_wind_speed_unit: Union[str, None]
    _weather_option_temperature_unit: Union[str, None]
    _weather_option_pressure_unit: Union[str, None]
    _weather_option_visibility_unit: Union[str, None]
    _weather_option_precipitation_unit: Union[str, None]
    _weather_option_wind_speed_unit: Union[str, None]
    def __init_subclass__(cls, **kwargs: Any) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    @property
    def temperature(self) -> Union[float, None]: ...
    @property
    def native_temperature(self) -> Union[float, None]: ...
    @property
    def native_temperature_unit(self) -> Union[str, None]: ...
    @property
    def temperature_unit(self) -> Union[str, None]: ...
    @property
    def _default_temperature_unit(self) -> str: ...
    @property
    def _temperature_unit(self) -> str: ...
    @property
    def pressure(self) -> Union[float, None]: ...
    @property
    def native_pressure(self) -> Union[float, None]: ...
    @property
    def native_pressure_unit(self) -> Union[str, None]: ...
    @property
    def pressure_unit(self) -> Union[str, None]: ...
    @property
    def _default_pressure_unit(self) -> str: ...
    @property
    def _pressure_unit(self) -> str: ...
    @property
    def humidity(self) -> Union[float, None]: ...
    @property
    def wind_speed(self) -> Union[float, None]: ...
    @property
    def native_wind_speed(self) -> Union[float, None]: ...
    @property
    def native_wind_speed_unit(self) -> Union[str, None]: ...
    @property
    def wind_speed_unit(self) -> Union[str, None]: ...
    @property
    def _default_wind_speed_unit(self) -> str: ...
    @property
    def _wind_speed_unit(self) -> str: ...
    @property
    def wind_bearing(self) -> Union[float, str, None]: ...
    @property
    def ozone(self) -> Union[float, None]: ...
    @property
    def visibility(self) -> Union[float, None]: ...
    @property
    def native_visibility(self) -> Union[float, None]: ...
    @property
    def native_visibility_unit(self) -> Union[str, None]: ...
    @property
    def visibility_unit(self) -> Union[str, None]: ...
    @property
    def _default_visibility_unit(self) -> str: ...
    @property
    def _visibility_unit(self) -> str: ...
    @property
    def forecast(self) -> Union[list[Forecast], None]: ...
    @property
    def native_precipitation_unit(self) -> Union[str, None]: ...
    @property
    def precipitation_unit(self) -> Union[str, None]: ...
    @property
    def _default_precipitation_unit(self) -> str: ...
    @property
    def _precipitation_unit(self) -> str: ...
    @property
    def precision(self) -> float: ...
    @property
    def state_attributes(self) -> dict[str, Any]: ...
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def condition(self) -> Union[str, None]: ...
    def async_registry_entry_updated(self) -> None: ...
