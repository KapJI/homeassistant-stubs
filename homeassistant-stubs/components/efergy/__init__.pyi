from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from pyefergy import Efergy

PLATFORMS: Incomplete
EfergyConfigEntry = ConfigEntry[Efergy]

async def async_setup_entry(hass: HomeAssistant, entry: EfergyConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: EfergyConfigEntry) -> bool: ...

class EfergyEntity(Entity):
    _attr_attribution: str
    api: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, api: Efergy, server_unique_id: str) -> None: ...
