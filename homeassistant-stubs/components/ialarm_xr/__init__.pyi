from .const import DOMAIN as DOMAIN
from .utils import async_get_ialarmxr_mac as async_get_ialarmxr_mac
from _typeshed import Incomplete
from homeassistant.components.alarm_control_panel import SCAN_INTERVAL as SCAN_INTERVAL
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyialarmxr import IAlarmXR

PLATFORMS: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class IAlarmXRDataUpdateCoordinator(DataUpdateCoordinator):
    ialarmxr: Incomplete
    state: Incomplete
    host: Incomplete
    mac: Incomplete
    def __init__(self, hass: HomeAssistant, ialarmxr: IAlarmXR, mac: str) -> None: ...
    def _update_data(self) -> None: ...
    async def _async_update_data(self) -> None: ...
