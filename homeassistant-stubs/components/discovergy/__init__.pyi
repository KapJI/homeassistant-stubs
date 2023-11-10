import pydiscovergy
from .const import DOMAIN as DOMAIN
from .coordinator import DiscovergyUpdateCoordinator as DiscovergyUpdateCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from pydiscovergy.models import Meter as Meter

PLATFORMS: Incomplete

@dataclass
class DiscovergyData:
    api_client: pydiscovergy.Discovergy
    meters: list[Meter]
    coordinators: dict[str, DiscovergyUpdateCoordinator]
    def __init__(self, api_client, meters, coordinators) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
