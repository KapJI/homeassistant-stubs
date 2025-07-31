from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pythonkuma import UptimeKumaMonitor, UptimeKumaVersion as UptimeKumaVersion
from pythonkuma.update import LatestRelease, UpdateChecker as UpdateChecker

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
SCAN_INTERVAL_UPDATES: Incomplete
type UptimeKumaConfigEntry = ConfigEntry[UptimeKumaDataUpdateCoordinator]

class UptimeKumaDataUpdateCoordinator(DataUpdateCoordinator[dict[str | int, UptimeKumaMonitor]]):
    config_entry: UptimeKumaConfigEntry
    api: Incomplete
    version: UptimeKumaVersion | None
    def __init__(self, hass: HomeAssistant, config_entry: UptimeKumaConfigEntry) -> None: ...
    async def _async_update_data(self) -> dict[str | int, UptimeKumaMonitor]: ...

@callback
def async_migrate_entities_unique_ids(hass: HomeAssistant, coordinator: UptimeKumaDataUpdateCoordinator, metrics: dict[str | int, UptimeKumaMonitor]) -> None: ...

class UptimeKumaSoftwareUpdateCoordinator(DataUpdateCoordinator[LatestRelease]):
    update_checker: Incomplete
    def __init__(self, hass: HomeAssistant, update_checker: UpdateChecker) -> None: ...
    async def _async_update_data(self) -> LatestRelease: ...
