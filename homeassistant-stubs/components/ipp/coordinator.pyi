from .const import CONF_BASE_PATH as CONF_BASE_PATH, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyipp import Printer as IPPPrinter

SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete
type IPPConfigEntry = ConfigEntry[IPPDataUpdateCoordinator]

class IPPDataUpdateCoordinator(DataUpdateCoordinator[IPPPrinter]):
    config_entry: IPPConfigEntry
    device_id: Incomplete
    ipp: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: IPPConfigEntry) -> None: ...
    async def _async_update_data(self) -> IPPPrinter: ...
