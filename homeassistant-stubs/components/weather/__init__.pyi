from homeassistant.const import PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from typing import Any

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
ATTR_FORECAST_CONDITION: str
ATTR_FORECAST_PRECIPITATION: str
ATTR_FORECAST_PRECIPITATION_PROBABILITY: str
ATTR_FORECAST_PRESSURE: str
ATTR_FORECAST_TEMP: str
ATTR_FORECAST_TEMP_LOW: str
ATTR_FORECAST_TIME: str
ATTR_FORECAST_WIND_BEARING: str
ATTR_FORECAST_WIND_SPEED: str
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

async def async_setup(hass: Any, config: Any): ...
async def async_setup_entry(hass: Any, entry: Any): ...
async def async_unload_entry(hass: Any, entry: Any): ...

class WeatherEntity(Entity):
    @property
    def temperature(self) -> None: ...
    @property
    def temperature_unit(self) -> None: ...
    @property
    def pressure(self) -> None: ...
    @property
    def humidity(self) -> None: ...
    @property
    def wind_speed(self) -> None: ...
    @property
    def wind_bearing(self) -> None: ...
    @property
    def ozone(self) -> None: ...
    @property
    def attribution(self) -> None: ...
    @property
    def visibility(self) -> None: ...
    @property
    def forecast(self) -> None: ...
    @property
    def precision(self): ...
    @property
    def state_attributes(self): ...
    @property
    def state(self): ...
    @property
    def condition(self) -> None: ...
