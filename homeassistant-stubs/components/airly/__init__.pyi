from .const import ATTR_API_ADVICE as ATTR_API_ADVICE, ATTR_API_CAQI as ATTR_API_CAQI, ATTR_API_CAQI_DESCRIPTION as ATTR_API_CAQI_DESCRIPTION, ATTR_API_CAQI_LEVEL as ATTR_API_CAQI_LEVEL, CONF_USE_NEAREST as CONF_USE_NEAREST, DOMAIN as DOMAIN, MAX_UPDATE_INTERVAL as MAX_UPDATE_INTERVAL, MIN_UPDATE_INTERVAL as MIN_UPDATE_INTERVAL, NO_AIRLY_SENSORS as NO_AIRLY_SENSORS
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

PLATFORMS: Incomplete
_LOGGER: Incomplete

def set_update_interval(instances_count: int, requests_remaining: int) -> timedelta: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class AirlyDataUpdateCoordinator(DataUpdateCoordinator):
    latitude: Incomplete
    longitude: Incomplete
    airly: Incomplete
    use_nearest: Incomplete
    def __init__(self, hass: HomeAssistant, session: ClientSession, api_key: str, latitude: float, longitude: float, update_interval: timedelta, use_nearest: bool) -> None: ...
    update_interval: Incomplete
    async def _async_update_data(self) -> dict[str, str | float | int]: ...
