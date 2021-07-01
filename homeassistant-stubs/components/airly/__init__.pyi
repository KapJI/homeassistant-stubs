from .const import ATTR_API_ADVICE as ATTR_API_ADVICE, ATTR_API_CAQI as ATTR_API_CAQI, ATTR_API_CAQI_DESCRIPTION as ATTR_API_CAQI_DESCRIPTION, ATTR_API_CAQI_LEVEL as ATTR_API_CAQI_LEVEL, CONF_USE_NEAREST as CONF_USE_NEAREST, DOMAIN as DOMAIN, MAX_UPDATE_INTERVAL as MAX_UPDATE_INTERVAL, MIN_UPDATE_INTERVAL as MIN_UPDATE_INTERVAL, NO_AIRLY_SENSORS as NO_AIRLY_SENSORS
from aiohttp import ClientSession as ClientSession
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import async_get_registry as async_get_registry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

PLATFORMS: Any
_LOGGER: Any

def set_update_interval(instances_count: int, requests_remaining: int) -> timedelta: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class AirlyDataUpdateCoordinator(DataUpdateCoordinator):
    latitude: Any
    longitude: Any
    airly: Any
    use_nearest: Any
    def __init__(self, hass: HomeAssistant, session: ClientSession, api_key: str, latitude: float, longitude: float, update_interval: timedelta, use_nearest: bool) -> None: ...
    update_interval: Any
    async def _async_update_data(self) -> dict[str, Union[str, float, int]]: ...
