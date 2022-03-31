from .const import CONF_STATION as CONF_STATION, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pytrafikverket.trafikverket_weather import WeatherStationInfo
from typing import Any

_LOGGER: Any
TIME_BETWEEN_UPDATES: Any

class TVDataUpdateCoordinator(DataUpdateCoordinator[WeatherStationInfo]):
    _weather_api: Any
    _station: Any
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> WeatherStationInfo: ...
