from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

DEFAULT_DEBOUNCER_COOLDOWN_SECONDS: Incomplete

class InvalidApiKeyMonitor:
    DEFAULT_FAILED_API_CALL_THRESHOLD: int
    _count: int
    _lock: Incomplete
    _reauth_flow_manager: Incomplete
    entry: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def async_increment(self) -> None: ...
    async def async_reset(self) -> None: ...

class ReauthFlowManager:
    entry: Incomplete
    hass: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    def _get_active_reauth_flow(self) -> Union[FlowResult, None]: ...
    def cancel_reauth(self) -> None: ...
    def start_reauth(self) -> None: ...

class OpenUvCoordinator(DataUpdateCoordinator):
    config_entry: ConfigEntry
    update_method: Callable[[], Awaitable[dict[str, Any]]]
    _invalid_api_key_monitor: Incomplete
    latitude: Incomplete
    longitude: Incomplete
    def __init__(self, hass: HomeAssistant, *, name: str, latitude: str, longitude: str, update_method: Callable[[], Awaitable[dict[str, Any]]], invalid_api_key_monitor: InvalidApiKeyMonitor) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
