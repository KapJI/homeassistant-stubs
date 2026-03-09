from .const import DOMAIN as DOMAIN
from .helpers import AuthFailed as AuthFailed, update_namecheapdns as update_namecheapdns
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN, CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
type NamecheapConfigEntry = ConfigEntry[NamecheapDnsUpdateCoordinator]
INTERVAL: Incomplete

class NamecheapDnsUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: NamecheapConfigEntry
    session: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: NamecheapConfigEntry) -> None: ...
    async def _async_update_data(self) -> None: ...
