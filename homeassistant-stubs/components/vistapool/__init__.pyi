from .const import DOMAIN as DOMAIN
from .coordinator import VistapoolDataUpdateCoordinator as VistapoolDataUpdateCoordinator
from _typeshed import Incomplete
from aioaquarite import AquariteAuth, AquariteClient
from dataclasses import dataclass, field
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_LOGGER: Incomplete
PLATFORMS: list[Platform]

@dataclass
class VistapoolData:
    auth: AquariteAuth
    api: AquariteClient
    coordinators: dict[str, VistapoolDataUpdateCoordinator] = field(default_factory=dict)
type VistapoolConfigEntry = ConfigEntry[VistapoolData]

async def async_setup_entry(hass: HomeAssistant, entry: VistapoolConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: VistapoolConfigEntry) -> bool: ...
