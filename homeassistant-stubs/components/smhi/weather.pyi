import aiohttp
from .const import ATTR_SMHI_CLOUDINESS as ATTR_SMHI_CLOUDINESS, ATTR_SMHI_THUNDER_PROBABILITY as ATTR_SMHI_THUNDER_PROBABILITY, ATTR_SMHI_WIND_GUST_SPEED as ATTR_SMHI_WIND_GUST_SPEED, DOMAIN as DOMAIN, ENTITY_ID_SENSOR_FORMAT as ENTITY_ID_SENSOR_FORMAT
from _typeshed import Incomplete
from collections.abc import Mapping
from datetime import datetime
from homeassistant.components.weather import ATTR_CONDITION_CLOUDY as ATTR_CONDITION_CLOUDY, ATTR_CONDITION_EXCEPTIONAL as ATTR_CONDITION_EXCEPTIONAL, ATTR_CONDITION_FOG as ATTR_CONDITION_FOG, ATTR_CONDITION_HAIL as ATTR_CONDITION_HAIL, ATTR_CONDITION_LIGHTNING as ATTR_CONDITION_LIGHTNING, ATTR_CONDITION_LIGHTNING_RAINY as ATTR_CONDITION_LIGHTNING_RAINY, ATTR_CONDITION_PARTLYCLOUDY as ATTR_CONDITION_PARTLYCLOUDY, ATTR_CONDITION_POURING as ATTR_CONDITION_POURING, ATTR_CONDITION_RAINY as ATTR_CONDITION_RAINY, ATTR_CONDITION_SNOWY as ATTR_CONDITION_SNOWY, ATTR_CONDITION_SNOWY_RAINY as ATTR_CONDITION_SNOWY_RAINY, ATTR_CONDITION_SUNNY as ATTR_CONDITION_SUNNY, ATTR_CONDITION_WINDY as ATTR_CONDITION_WINDY, ATTR_CONDITION_WINDY_VARIANT as ATTR_CONDITION_WINDY_VARIANT, ATTR_FORECAST_CONDITION as ATTR_FORECAST_CONDITION, ATTR_FORECAST_NATIVE_PRECIPITATION as ATTR_FORECAST_NATIVE_PRECIPITATION, ATTR_FORECAST_NATIVE_PRESSURE as ATTR_FORECAST_NATIVE_PRESSURE, ATTR_FORECAST_NATIVE_TEMP as ATTR_FORECAST_NATIVE_TEMP, ATTR_FORECAST_NATIVE_TEMP_LOW as ATTR_FORECAST_NATIVE_TEMP_LOW, ATTR_FORECAST_NATIVE_WIND_SPEED as ATTR_FORECAST_NATIVE_WIND_SPEED, ATTR_FORECAST_TIME as ATTR_FORECAST_TIME, ATTR_FORECAST_WIND_BEARING as ATTR_FORECAST_WIND_BEARING, Forecast as Forecast, ROUNDING_PRECISION as ROUNDING_PRECISION, WeatherEntity as WeatherEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LOCATION as CONF_LOCATION, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME, LENGTH_KILOMETERS as LENGTH_KILOMETERS, LENGTH_MILLIMETERS as LENGTH_MILLIMETERS, PRESSURE_HPA as PRESSURE_HPA, SPEED_METERS_PER_SECOND as SPEED_METERS_PER_SECOND, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.util import Throttle as Throttle, slugify as slugify
from homeassistant.util.unit_conversion import SpeedConverter as SpeedConverter
from smhi.smhi_lib import SmhiForecast as SmhiForecast
from typing import Any, Final

_LOGGER: Incomplete
CONDITION_CLASSES: Final[dict[str, list[int]]]
TIMEOUT: int
RETRY_TIMEOUT: Incomplete
MIN_TIME_BETWEEN_UPDATES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SmhiWeather(WeatherEntity):
    _attr_attribution: str
    _attr_native_temperature_unit: Incomplete
    _attr_native_visibility_unit: Incomplete
    _attr_native_precipitation_unit: Incomplete
    _attr_native_wind_speed_unit: Incomplete
    _attr_native_pressure_unit: Incomplete
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _forecasts: Incomplete
    _fail_count: int
    _smhi_api: Incomplete
    _attr_device_info: Incomplete
    _attr_condition: Incomplete
    _attr_native_temperature: Incomplete
    def __init__(self, name: str, latitude: str, longitude: str, session: aiohttp.ClientSession) -> None: ...
    @property
    def extra_state_attributes(self) -> Union[Mapping[str, Any], None]: ...
    _attr_humidity: Incomplete
    _attr_native_wind_speed: Incomplete
    _attr_wind_bearing: Incomplete
    _attr_native_visibility: Incomplete
    _attr_native_pressure: Incomplete
    async def async_update(self) -> None: ...
    async def retry_update(self, _: datetime) -> None: ...
    @property
    def forecast(self) -> Union[list[Forecast], None]: ...
