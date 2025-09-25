from .const import CONNECT_DELAY as CONNECT_DELAY, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_CODE as CONF_CODE, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

VERSION_TIMEOUT: int
_LOGGER: Incomplete
TIMEOUT: int
type DropletConfigEntry = ConfigEntry[DropletDataCoordinator]

class DropletDataCoordinator(DataUpdateCoordinator[None]):
    config_entry: DropletConfigEntry
    droplet: Incomplete
    unique_id: Incomplete
    def __init__(self, hass: HomeAssistant, entry: DropletConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> None: ...
    async def setup(self) -> bool: ...
    def get_availability(self) -> bool: ...
