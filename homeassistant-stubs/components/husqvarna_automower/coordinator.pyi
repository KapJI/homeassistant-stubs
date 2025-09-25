import asyncio
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioautomower.model import MowerDictionary
from aioautomower.session import AutomowerSession as AutomowerSession
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

_LOGGER: Incomplete
MAX_WS_RECONNECT_TIME: int
SCAN_INTERVAL: Incomplete
DEFAULT_RECONNECT_TIME: int
PING_INTERVAL: int
type AutomowerConfigEntry = ConfigEntry[AutomowerDataUpdateCoordinator]

class AutomowerDataUpdateCoordinator(DataUpdateCoordinator[MowerDictionary]):
    config_entry: AutomowerConfigEntry
    api: Incomplete
    reconnect_time: Incomplete
    new_devices_callbacks: list[Callable[[set[str]], None]]
    new_zones_callbacks: list[Callable[[str, set[str]], None]]
    new_areas_callbacks: list[Callable[[str, set[int]], None]]
    pong: datetime | None
    websocket_alive: bool
    websocket_callbacks: list[Callable[[bool], None]]
    _watchdog_task: asyncio.Task | None
    def __init__(self, hass: HomeAssistant, config_entry: AutomowerConfigEntry, api: AutomowerSession) -> None: ...
    @override
    @callback
    def async_update_listeners(self) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> MowerDictionary: ...
    update_interval: Incomplete
    @callback
    def _on_data_update(self) -> None: ...
    @callback
    def handle_websocket_updates(self, ws_data: MowerDictionary) -> None: ...
    async def _process_websocket_update(self, ws_data: MowerDictionary) -> None: ...
    data: Incomplete
    last_update_success: bool
    @callback
    def async_set_updated_data(self, data: MowerDictionary) -> None: ...
    async def client_listen(self, hass: HomeAssistant, entry: AutomowerConfigEntry, automower_client: AutomowerSession) -> None: ...
    def _should_poll(self) -> bool: ...
    async def _pong_watchdog(self) -> None: ...
    def _async_add_remove_devices(self) -> None: ...
    def _async_add_remove_stay_out_zones(self) -> None: ...
    def _async_add_remove_work_areas(self) -> None: ...
