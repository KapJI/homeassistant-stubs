from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from python_overseerr import RequestCount

type OverseerrConfigEntry = ConfigEntry[OverseerrCoordinator]
class OverseerrCoordinator(DataUpdateCoordinator[RequestCount]):
    config_entry: OverseerrConfigEntry
    client: Incomplete
    url: Incomplete
    push: bool
    def __init__(self, hass: HomeAssistant, entry: OverseerrConfigEntry) -> None: ...
    async def _async_update_data(self) -> RequestCount: ...
