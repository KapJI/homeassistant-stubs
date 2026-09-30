from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SESSION_HISTORY_WINDOW as SESSION_HISTORY_WINDOW, UPDATE_REBOOT_MINIMUM_DOWNTIME as UPDATE_REBOOT_MINIMUM_DOWNTIME, UPDATE_REBOOT_RETURN_TIMEOUT as UPDATE_REBOOT_RETURN_TIMEOUT, UPDATE_REBOOT_START_TIMEOUT as UPDATE_REBOOT_START_TIMEOUT
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from datetime import datetime, timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from peblar import Peblar as Peblar, PeblarApi as PeblarApi, PeblarEVInterface as PeblarEVInterface, PeblarMeter as PeblarMeter, PeblarSystem as PeblarSystem, PeblarSystemInformation as PeblarSystemInformation, PeblarUserConfiguration, PeblarVersions as PeblarVersions
from typing import Any, Concatenate, override

@dataclass(kw_only=True)
class PeblarRuntimeData:
    authorization_coordinator: PeblarAuthorizationDataUpdateCoordinator
    data_coordinator: PeblarDataUpdateCoordinator
    last_known_charging_limit = ...
    system_information: PeblarSystemInformation
    user_configuration_coordinator: PeblarUserConfigurationDataUpdateCoordinator
    version_coordinator: PeblarVersionDataUpdateCoordinator
type PeblarConfigEntry = ConfigEntry[PeblarRuntimeData]

@dataclass(kw_only=True, frozen=True)
class PeblarSessionAuthorization:
    session_number: int
    started_at: datetime
    token: str

@dataclass(kw_only=True, frozen=True)
class PeblarVersionInformation:
    current: PeblarVersions
    available: PeblarVersions

@dataclass(kw_only=True)
class PeblarData:
    ev: PeblarEVInterface
    meter: PeblarMeter
    system: PeblarSystem

def _coordinator_exception_handler[_DataUpdateCoordinatorT: PeblarDataUpdateCoordinator | PeblarVersionDataUpdateCoordinator | PeblarUserConfigurationDataUpdateCoordinator | PeblarAuthorizationDataUpdateCoordinator, **_P](func: Callable[Concatenate[_DataUpdateCoordinatorT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_DataUpdateCoordinatorT, _P], Coroutine[Any, Any, Any]]: ...

class PeblarVersionDataUpdateCoordinator(DataUpdateCoordinator[PeblarVersionInformation]):
    config_entry: PeblarConfigEntry
    install_in_progress: bool
    peblar: Incomplete
    _reboot_watcher: _RebootWatcher | None
    def __init__(self, hass: HomeAssistant, entry: PeblarConfigEntry, peblar: Peblar) -> None: ...
    @_coordinator_exception_handler
    @override
    async def _async_update_data(self) -> PeblarVersionInformation: ...
    @callback
    def async_refresh_after_restart(self) -> None: ...
    @callback
    def async_stop_reboot_watcher(self) -> None: ...

class PeblarAuthorizationDataUpdateCoordinator(DataUpdateCoordinator[PeblarSessionAuthorization | None]):
    peblar: Incomplete
    def __init__(self, hass: HomeAssistant, entry: PeblarConfigEntry, peblar: Peblar) -> None: ...
    @_coordinator_exception_handler
    @override
    async def _async_update_data(self) -> PeblarSessionAuthorization | None: ...

class _RebootWatcher:
    _coordinator: Incomplete
    _entry: Incomplete
    _data_coordinator: Incomplete
    _went_down_at: datetime | None
    _start_deadline: datetime | None
    _unsubscribe_listener: CALLBACK_TYPE | None
    _unsubscribe_timer: CALLBACK_TYPE | None
    def __init__(self, coordinator: PeblarVersionDataUpdateCoordinator) -> None: ...
    @callback
    def async_start(self) -> None: ...
    @callback
    def _async_set_deadline(self, timeout: timedelta) -> None: ...
    @callback
    def _handle_deadline(self, _now: datetime) -> None: ...
    @callback
    def _async_unsubscribe(self) -> None: ...
    @callback
    def async_stop(self) -> None: ...
    @callback
    def _handle_data_coordinator_update(self) -> None: ...
    async def _async_finish(self) -> None: ...

class PeblarDataUpdateCoordinator(DataUpdateCoordinator[PeblarData]):
    config_entry: PeblarConfigEntry
    api: Incomplete
    def __init__(self, hass: HomeAssistant, entry: PeblarConfigEntry, api: PeblarApi) -> None: ...
    @_coordinator_exception_handler
    @override
    async def _async_update_data(self) -> PeblarData: ...

class PeblarUserConfigurationDataUpdateCoordinator(DataUpdateCoordinator[PeblarUserConfiguration]):
    peblar: Incomplete
    def __init__(self, hass: HomeAssistant, entry: PeblarConfigEntry, peblar: Peblar) -> None: ...
    @_coordinator_exception_handler
    @override
    async def _async_update_data(self) -> PeblarUserConfiguration: ...
