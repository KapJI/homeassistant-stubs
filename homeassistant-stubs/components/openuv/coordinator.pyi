import datetime as dt
from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.dt import parse_datetime as parse_datetime, utcnow as utcnow
from typing import Any

DEFAULT_DEBOUNCER_COOLDOWN_SECONDS: Incomplete

class OpenUvCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: ConfigEntry
    update_method: Callable[[], Awaitable[dict[str, Any]]]
    latitude: Incomplete
    longitude: Incomplete
    def __init__(self, hass: HomeAssistant, *, entry: ConfigEntry, name: str, latitude: str, longitude: str, update_method: Callable[[], Awaitable[dict[str, Any]]]) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...

class OpenUvProtectionWindowCoordinator(OpenUvCoordinator):
    _reprocess_listener: CALLBACK_TYPE | None
    async def _async_update_data(self) -> dict[str, Any]: ...
    def _parse_data(self, data: dict[str, Any]) -> dict[str, Any]: ...
    def _process_data(self, data: dict[str, Any]) -> dict[str, Any]: ...
    def _schedule_reprocessing(self, data: dict[str, Any]) -> None: ...
    def _async_cancel_reprocess_listener(self) -> None: ...
    data: Incomplete
    @callback
    def _async_handle_reprocess_event(self, now: dt.datetime) -> None: ...
