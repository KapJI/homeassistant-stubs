from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioautomower.model import MowerAttributes
from aioautomower.session import AutomowerSession as AutomowerSession
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
MAX_WS_RECONNECT_TIME: int
SCAN_INTERVAL: Incomplete

class AutomowerDataUpdateCoordinator(DataUpdateCoordinator[dict[str, MowerAttributes]]):
    api: Incomplete
    ws_connected: bool
    def __init__(self, hass: HomeAssistant, api: AutomowerSession, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> dict[str, MowerAttributes]: ...
    def callback(self, ws_data: dict[str, MowerAttributes]) -> None: ...
    async def client_listen(self, hass: HomeAssistant, entry: ConfigEntry, automower_client: AutomowerSession, reconnect_time: int = 2) -> None: ...
