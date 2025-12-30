from .const import DOMAIN as DOMAIN
from .helpers import update_duckdns as update_duckdns
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_DOMAIN as CONF_DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
type DuckDnsConfigEntry = ConfigEntry[DuckDnsUpdateCoordinator]
INTERVAL: Incomplete
BACKOFF_INTERVALS: Incomplete

class DuckDnsUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: DuckDnsConfigEntry
    session: Incomplete
    failed: int
    def __init__(self, hass: HomeAssistant, config_entry: DuckDnsConfigEntry) -> None: ...
    async def _async_update_data(self) -> None: ...
