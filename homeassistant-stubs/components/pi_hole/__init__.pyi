from .const import CONF_LOCATION as CONF_LOCATION, CONF_STATISTICS_ONLY as CONF_STATISTICS_ONLY, DATA_KEY_API as DATA_KEY_API, DATA_KEY_COORDINATOR as DATA_KEY_COORDINATOR, DEFAULT_LOCATION as DEFAULT_LOCATION, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_SSL as DEFAULT_SSL, DEFAULT_VERIFY_SSL as DEFAULT_VERIFY_SSL, DOMAIN as DOMAIN, MIN_TIME_BETWEEN_UPDATES as MIN_TIME_BETWEEN_UPDATES
from hole import Hole
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_SSL as CONF_SSL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Any
PI_HOLE_SCHEMA: Any
CONFIG_SCHEMA: Any

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def _async_platforms(entry: ConfigEntry) -> list[str]: ...

class PiHoleEntity(CoordinatorEntity):
    api: Any
    _name: Any
    _server_unique_id: Any
    def __init__(self, api: Hole, coordinator: DataUpdateCoordinator, name: str, server_unique_id: str) -> None: ...
    @property
    def icon(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
