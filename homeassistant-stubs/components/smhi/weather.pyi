import aiohttp
from .const import ATTR_SMHI_CLOUDINESS as ATTR_SMHI_CLOUDINESS, ATTR_SMHI_THUNDER_PROBABILITY as ATTR_SMHI_THUNDER_PROBABILITY, ATTR_SMHI_WIND_GUST_SPEED as ATTR_SMHI_WIND_GUST_SPEED, DOMAIN as DOMAIN, ENTITY_ID_SENSOR_FORMAT as ENTITY_ID_SENSOR_FORMAT
from datetime import datetime
from homeassistant.components.weather import ATTR_CONDITION_CLOUDY as ATTR_CONDITION_CLOUDY, ATTR_CONDITION_EXCEPTIONAL as ATTR_CONDITION_EXCEPTIONAL, ATTR_CONDITION_FOG as ATTR_CONDITION_FOG, ATTR_CONDITION_HAIL as ATTR_CONDITION_HAIL, ATTR_CONDITION_LIGHTNING as ATTR_CONDITION_LIGHTNING, ATTR_CONDITION_LIGHTNING_RAINY as ATTR_CONDITION_LIGHTNING_RAINY, ATTR_CONDITION_PARTLYCLOUDY as ATTR_CONDITION_PARTLYCLOUDY, ATTR_CONDITION_POURING as ATTR_CONDITION_POURING, ATTR_CONDITION_RAINY as ATTR_CONDITION_RAINY, ATTR_CONDITION_SNOWY as ATTR_CONDITION_SNOWY, ATTR_CONDITION_SNOWY_RAINY as ATTR_CONDITION_SNOWY_RAINY, ATTR_CONDITION_SUNNY as ATTR_CONDITION_SUNNY, ATTR_CONDITION_WINDY as ATTR_CONDITION_WINDY, ATTR_CONDITION_WINDY_VARIANT as ATTR_CONDITION_WINDY_VARIANT, ATTR_FORECAST_CONDITION as ATTR_FORECAST_CONDITION, ATTR_FORECAST_PRECIPITATION as ATTR_FORECAST_PRECIPITATION, ATTR_FORECAST_TEMP as ATTR_FORECAST_TEMP, ATTR_FORECAST_TEMP_LOW as ATTR_FORECAST_TEMP_LOW, ATTR_FORECAST_TIME as ATTR_FORECAST_TIME, Forecast as Forecast, WeatherEntity as WeatherEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME, LENGTH_KILOMETERS as LENGTH_KILOMETERS, LENGTH_MILLIMETERS as LENGTH_MILLIMETERS, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.util import Throttle as Throttle, slugify as slugify
from smhi.smhi_lib import SmhiForecast as SmhiForecast
from typing import Any, Final

_LOGGER: Any
CONDITION_CLASSES: Final[dict[str, list[int]]]
TIMEOUT: int
RETRY_TIMEOUT: Any
MIN_TIME_BETWEEN_UPDATES: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SmhiWeather(WeatherEntity):
    _attr_attribution: str
    _attr_temperature_unit: Any
    _attr_visibility_unit: Any
    _attr_precipitation_unit: Any
    _attr_name: Any
    _attr_unique_id: Any
    _forecasts: Any
    _fail_count: int
    _smhi_api: Any
    _attr_device_info: Any
    _attr_condition: Any
    _attr_temperature: Any
    def __init__(self, name: str, latitude: str, longitude: str, session: aiohttp.ClientSession) -> None: ...
    _attr_humidity: Any
    _attr_wind_speed: Any
    _attr_wind_bearing: Any
    _attr_visibility: Any
    _attr_pressure: Any
    _attr_extra_state_attributes: Any
    async def async_update(self) -> None: ...
    async def retry_update(self, _: datetime) -> None: ...
    @property
    def forecast(self) -> Union[list[Forecast], None]: ...
