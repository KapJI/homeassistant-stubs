from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from openevsehttp.__main__ import OpenEVSE as OpenEVSE

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
type OpenEVSEConfigEntry = ConfigEntry[OpenEVSEDataUpdateCoordinator]

class OpenEVSEDataUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: OpenEVSEConfigEntry
    charger: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: OpenEVSEConfigEntry, charger: OpenEVSE) -> None: ...
    async def _async_websocket_callback(self) -> None: ...
    def start_websocket(self) -> None: ...
    async def async_stop_websocket(self) -> None: ...
    async def _async_update_data(self) -> None: ...
