import meteireann
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ELEVATION as CONF_ELEVATION, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any, Self

_LOGGER: Incomplete
UPDATE_INTERVAL: Incomplete

class MetEireannWeatherData:
    _config: Incomplete
    _weather_data: Incomplete
    current_weather_data: dict[str, Any]
    daily_forecast: list[dict[str, Any]]
    hourly_forecast: list[dict[str, Any]]
    def __init__(self, config: Mapping[str, Any], weather_data: meteireann.WeatherData) -> None: ...
    async def fetch_data(self) -> Self: ...

class MetEireannUpdateCoordinator(DataUpdateCoordinator[MetEireannWeatherData]):
    config_entry: ConfigEntry
    _weather_data: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> MetEireannWeatherData: ...
