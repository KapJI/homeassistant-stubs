from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SCAN_INTERVAL as SCAN_INTERVAL
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from whois import Domain

class WhoisCoordinator(DataUpdateCoordinator[Domain | None]):
    config_entry: ConfigEntry
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> Domain | None: ...
