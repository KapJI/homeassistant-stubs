from .const import ATTR_WEATHER_APPARENT_TEMPERATURE as ATTR_WEATHER_APPARENT_TEMPERATURE, ATTR_WEATHER_CLOUD_COVERAGE as ATTR_WEATHER_CLOUD_COVERAGE, ATTR_WEATHER_DEW_POINT as ATTR_WEATHER_DEW_POINT, ATTR_WEATHER_HUMIDITY as ATTR_WEATHER_HUMIDITY, ATTR_WEATHER_OZONE as ATTR_WEATHER_OZONE, ATTR_WEATHER_PRECIPITATION_UNIT as ATTR_WEATHER_PRECIPITATION_UNIT, ATTR_WEATHER_PRESSURE as ATTR_WEATHER_PRESSURE, ATTR_WEATHER_PRESSURE_UNIT as ATTR_WEATHER_PRESSURE_UNIT, ATTR_WEATHER_TEMPERATURE as ATTR_WEATHER_TEMPERATURE, ATTR_WEATHER_TEMPERATURE_UNIT as ATTR_WEATHER_TEMPERATURE_UNIT, ATTR_WEATHER_VISIBILITY as ATTR_WEATHER_VISIBILITY, ATTR_WEATHER_VISIBILITY_UNIT as ATTR_WEATHER_VISIBILITY_UNIT, ATTR_WEATHER_WIND_BEARING as ATTR_WEATHER_WIND_BEARING, ATTR_WEATHER_WIND_GUST_SPEED as ATTR_WEATHER_WIND_GUST_SPEED, ATTR_WEATHER_WIND_SPEED as ATTR_WEATHER_WIND_SPEED, ATTR_WEATHER_WIND_SPEED_UNIT as ATTR_WEATHER_WIND_SPEED_UNIT, DOMAIN as DOMAIN, UNIT_CONVERSIONS as UNIT_CONVERSIONS, VALID_UNITS as VALID_UNITS
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PRECISION_HALVES as PRECISION_HALVES, PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
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
ATTR_FORECAST_HUMIDITY: Final[str]
ATTR_FORECAST_NATIVE_PRECIPITATION: Final[str]
ATTR_FORECAST_PRECIPITATION: Final[str]
ATTR_FORECAST_PRECIPITATION_PROBABILITY: Final[str]
ATTR_FORECAST_NATIVE_PRESSURE: Final[str]
ATTR_FORECAST_PRESSURE: Final[str]
ATTR_FORECAST_NATIVE_APPARENT_TEMP: Final[str]
ATTR_FORECAST_APPARENT_TEMP: Final[str]
ATTR_FORECAST_NATIVE_TEMP: Final[str]
ATTR_FORECAST_TEMP: Final[str]
ATTR_FORECAST_NATIVE_TEMP_LOW: Final[str]
ATTR_FORECAST_TEMP_LOW: Final[str]
ATTR_FORECAST_TIME: Final[str]
ATTR_FORECAST_WIND_BEARING: Final[str]
ATTR_FORECAST_NATIVE_WIND_GUST_SPEED: Final[str]
ATTR_FORECAST_WIND_GUST_SPEED: Final[str]
ATTR_FORECAST_NATIVE_WIND_SPEED: Final[str]
ATTR_FORECAST_WIND_SPEED: Final[str]
ATTR_FORECAST_NATIVE_DEW_POINT: Final[str]
ATTR_FORECAST_DEW_POINT: Final[str]
ATTR_FORECAST_CLOUD_COVERAGE: Final[str]
ENTITY_ID_FORMAT: Incomplete
SCAN_INTERVAL: Incomplete
ROUNDING_PRECISION: int

def round_temperature(temperature: float | None, precision: float) -> float | None: ...

class Forecast(TypedDict, total=False):
    condition: str | None
    datetime: Required[str]
    humidity: float | None
    precipitation_probability: int | None
    cloud_coverage: int | None
    native_precipitation: float | None
    precipitation: None
    native_pressure: float | None
    pressure: None
    native_temperature: float | None
    temperature: None
    native_templow: float | None
    templow: None
    native_apparent_temperature: float | None
    wind_bearing: float | str | None
    native_wind_gust_speed: float | None
    native_wind_speed: float | None
    wind_speed: None
    native_dew_point: float | None

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class WeatherEntityDescription(EntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class WeatherEntity(Entity):
    entity_description: WeatherEntityDescription
    _attr_condition: str | None
    _attr_forecast: list[Forecast] | None
    _attr_humidity: float | None
    _attr_ozone: float | None
    _attr_cloud_coverage: int | None
    _attr_precision: float
    _attr_pressure: None
    _attr_pressure_unit: None
    _attr_state: None
    _attr_temperature: None
    _attr_temperature_unit: None
    _attr_visibility: None
    _attr_visibility_unit: None
    _attr_precipitation_unit: None
    _attr_wind_bearing: float | str | None
    _attr_wind_speed: None
    _attr_wind_speed_unit: None
    _attr_native_pressure: float | None
    _attr_native_pressure_unit: str | None
    _attr_native_apparent_temperature: float | None
    _attr_native_temperature: float | None
    _attr_native_temperature_unit: str | None
    _attr_native_visibility: float | None
    _attr_native_visibility_unit: str | None
    _attr_native_precipitation_unit: str | None
    _attr_native_wind_gust_speed: float | None
    _attr_native_wind_speed: float | None
    _attr_native_wind_speed_unit: str | None
    _attr_native_dew_point: float | None
    _weather_option_temperature_unit: str | None
    _weather_option_pressure_unit: str | None
    _weather_option_visibility_unit: str | None
    _weather_option_precipitation_unit: str | None
    _weather_option_wind_speed_unit: str | None
    def __init_subclass__(cls, **kwargs: Any) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    @property
    def native_apparent_temperature(self) -> float | None: ...
    @property
    def temperature(self) -> float | None: ...
    @property
    def native_temperature(self) -> float | None: ...
    @property
    def native_temperature_unit(self) -> str | None: ...
    @property
    def native_dew_point(self) -> float | None: ...
    @property
    def temperature_unit(self) -> str | None: ...
    @property
    def _default_temperature_unit(self) -> str: ...
    @property
    def _temperature_unit(self) -> str: ...
    @property
    def pressure(self) -> float | None: ...
    @property
    def native_pressure(self) -> float | None: ...
    @property
    def native_pressure_unit(self) -> str | None: ...
    @property
    def pressure_unit(self) -> str | None: ...
    @property
    def _default_pressure_unit(self) -> str: ...
    @property
    def _pressure_unit(self) -> str: ...
    @property
    def humidity(self) -> float | None: ...
    @property
    def native_wind_gust_speed(self) -> float | None: ...
    @property
    def wind_speed(self) -> float | None: ...
    @property
    def native_wind_speed(self) -> float | None: ...
    @property
    def native_wind_speed_unit(self) -> str | None: ...
    @property
    def wind_speed_unit(self) -> str | None: ...
    @property
    def _default_wind_speed_unit(self) -> str: ...
    @property
    def _wind_speed_unit(self) -> str: ...
    @property
    def wind_bearing(self) -> float | str | None: ...
    @property
    def ozone(self) -> float | None: ...
    @property
    def cloud_coverage(self) -> float | None: ...
    @property
    def visibility(self) -> float | None: ...
    @property
    def native_visibility(self) -> float | None: ...
    @property
    def native_visibility_unit(self) -> str | None: ...
    @property
    def visibility_unit(self) -> str | None: ...
    @property
    def _default_visibility_unit(self) -> str: ...
    @property
    def _visibility_unit(self) -> str: ...
    @property
    def forecast(self) -> list[Forecast] | None: ...
    @property
    def native_precipitation_unit(self) -> str | None: ...
    @property
    def precipitation_unit(self) -> str | None: ...
    @property
    def _default_precipitation_unit(self) -> str: ...
    @property
    def _precipitation_unit(self) -> str: ...
    @property
    def precision(self) -> float: ...
    @property
    def state_attributes(self) -> dict[str, Any]: ...
    @property
    def state(self) -> str | None: ...
    @property
    def condition(self) -> str | None: ...
    def async_registry_entry_updated(self) -> None: ...
