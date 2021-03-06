from .const import ATTR_SDS011 as ATTR_SDS011, ATTR_SPS30 as ATTR_SPS30, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_UPDATE_INTERVAL as DEFAULT_UPDATE_INTERVAL, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from aiohttp import ClientSession as ClientSession
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from nettigo_air_monitor import NAMSensors as NAMSensors
from typing import Any

_LOGGER: Any
PLATFORMS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class NAMDataUpdateCoordinator(DataUpdateCoordinator):
    host: Any
    nam: Any
    _unique_id: Any
    def __init__(self, hass: HomeAssistant, session: ClientSession, host: str, unique_id: Union[str, None]) -> None: ...
    async def _async_update_data(self) -> NAMSensors: ...
    @property
    def unique_id(self) -> Union[str, None]: ...
    @property
    def device_info(self) -> DeviceInfo: ...
