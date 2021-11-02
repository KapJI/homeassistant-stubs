from .const import ATTRIBUTION as ATTRIBUTION, DATA_KEY_API as DATA_KEY_API, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from pyefergy import Efergy
from typing import Any

PLATFORMS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class EfergyEntity(Entity):
    api: Any
    _server_unique_id: Any
    _attr_extra_state_attributes: Any
    _attr_device_info: Any
    def __init__(self, api: Efergy, server_unique_id: str) -> None: ...
