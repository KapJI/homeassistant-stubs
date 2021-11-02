from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from typing import Any, Final, TypedDict

_LOGGER: Any
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
ATTR_FORECAST_PRECIPITATION: Final[str]
ATTR_FORECAST_PRECIPITATION_PROBABILITY: Final[str]
ATTR_FORECAST_PRESSURE: Final[str]
ATTR_FORECAST_TEMP: Final[str]
ATTR_FORECAST_TEMP_LOW: Final[str]
ATTR_FORECAST_TIME: Final[str]
ATTR_FORECAST_WIND_BEARING: Final[str]
ATTR_FORECAST_WIND_SPEED: Final[str]
ATTR_WEATHER_ATTRIBUTION: str
ATTR_WEATHER_HUMIDITY: str
ATTR_WEATHER_OZONE: str
ATTR_WEATHER_PRESSURE: str
ATTR_WEATHER_TEMPERATURE: str
ATTR_WEATHER_VISIBILITY: str
ATTR_WEATHER_WIND_BEARING: str
ATTR_WEATHER_WIND_SPEED: str
DOMAIN: str
ENTITY_ID_FORMAT: Any
SCAN_INTERVAL: Any

class Forecast(TypedDict):
    condition: Union[str, None]
    datetime: str
    precipitation_probability: Union[int, None]
    precipitation: Union[float, None]
    pressure: Union[float, None]
    temperature: Union[float, None]
    templow: Union[float, None]
    wind_bearing: Union[float, str, None]
    wind_speed: Union[float, None]

async def async_setup(hass, config): ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class WeatherEntityDescription(EntityDescription): ...

class WeatherEntity(Entity):
    entity_description: WeatherEntityDescription
    _attr_attribution: Union[str, None]
    _attr_condition: Union[str, None]
    _attr_forecast: Union[list[Forecast], None]
    _attr_humidity: Union[float, None]
    _attr_ozone: Union[float, None]
    _attr_precision: float
    _attr_pressure: Union[float, None]
    _attr_state: None
    _attr_temperature_unit: str
    _attr_temperature: Union[float, None]
    _attr_visibility: Union[float, None]
    _attr_wind_bearing: Union[float, str, None]
    _attr_wind_speed: Union[float, None]
    @property
    def temperature(self) -> Union[float, None]: ...
    @property
    def temperature_unit(self) -> str: ...
    @property
    def pressure(self) -> Union[float, None]: ...
    @property
    def humidity(self) -> Union[float, None]: ...
    @property
    def wind_speed(self) -> Union[float, None]: ...
    @property
    def wind_bearing(self) -> Union[float, str, None]: ...
    @property
    def ozone(self) -> Union[float, None]: ...
    @property
    def attribution(self) -> Union[str, None]: ...
    @property
    def visibility(self) -> Union[float, None]: ...
    @property
    def forecast(self) -> Union[list[Forecast], None]: ...
    @property
    def precision(self) -> float: ...
    @property
    def state_attributes(self): ...
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def condition(self) -> Union[str, None]: ...
