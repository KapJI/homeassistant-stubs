from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioautomower.model import MowerDictionary
from aioautomower.session import AutomowerSession as AutomowerSession
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
MAX_WS_RECONNECT_TIME: int
SCAN_INTERVAL: Incomplete
DEFAULT_RECONNECT_TIME: int
type AutomowerConfigEntry = ConfigEntry[AutomowerDataUpdateCoordinator]

class AutomowerDataUpdateCoordinator(DataUpdateCoordinator[MowerDictionary]):
    config_entry: AutomowerConfigEntry
    api: Incomplete
    ws_connected: bool
    reconnect_time: Incomplete
    new_devices_callbacks: list[Callable[[set[str]], None]]
    new_zones_callbacks: list[Callable[[str, set[str]], None]]
    new_areas_callbacks: list[Callable[[str, set[int]], None]]
    _devices_last_update: set[str]
    _zones_last_update: dict[str, set[str]]
    _areas_last_update: dict[str, set[int]]
    def __init__(self, hass: HomeAssistant, config_entry: AutomowerConfigEntry, api: AutomowerSession) -> None: ...
    def _async_add_remove_devices_and_entities(self, data: MowerDictionary) -> None: ...
    async def _async_update_data(self) -> MowerDictionary: ...
    @callback
    def callback(self, ws_data: MowerDictionary) -> None: ...
    async def client_listen(self, hass: HomeAssistant, entry: AutomowerConfigEntry, automower_client: AutomowerSession) -> None: ...
    data: Incomplete
    def _async_add_remove_devices(self, data: MowerDictionary) -> None: ...
    def _remove_device(self, removed_devices: set[str]) -> None: ...
    def _add_new_devices(self, new_devices: set[str]) -> None: ...
    def _async_add_remove_stay_out_zones(self, data: MowerDictionary) -> None: ...
    def _update_stay_out_zones(self, current_zones: dict[str, set[str]]) -> dict[str, set[str]]: ...
    def _async_add_remove_work_areas(self, data: MowerDictionary) -> None: ...
    def _update_work_areas(self, current_areas: dict[str, set[int]]) -> dict[str, set[int]]: ...
