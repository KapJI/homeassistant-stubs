import asyncio
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass, field
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyliebherrhomeapi import DeviceControl as DeviceControl, DeviceState, LiebherrClient as LiebherrClient
from typing import override

_LOGGER: Incomplete

@dataclass
class LiebherrData:
    client: LiebherrClient
    coordinators: dict[str, LiebherrCoordinator] = field(default_factory=dict)
type LiebherrConfigEntry = ConfigEntry[LiebherrData]

class LiebherrCoordinator(DataUpdateCoordinator[DeviceState]):
    config_entry: LiebherrConfigEntry
    client: Incomplete
    device_id: Incomplete
    _stream_task: asyncio.Task[None] | None
    _replace_next_event: bool
    def __init__(self, hass: HomeAssistant, config_entry: LiebherrConfigEntry, client: LiebherrClient, device_id: str) -> None: ...
    @override
    async def _async_setup(self) -> None: ...
    @override
    async def _async_update_data(self) -> DeviceState: ...
    @callback
    def async_start_stream(self) -> None: ...
    async def _async_run_stream(self) -> None: ...
    @override
    async def async_shutdown(self) -> None: ...
    def _apply_controls(self, controls: list[DeviceControl]) -> None: ...
    data: Incomplete
    @callback
    def async_apply_control[ControlT: DeviceControl](self, control: ControlT, updater: Callable[[ControlT], ControlT]) -> None: ...
    def _merged_state(self, controls: list[DeviceControl]) -> DeviceState: ...
    @callback
    def _handle_stream_connected(self) -> None: ...
    @callback
    def _handle_stream_disconnected(self) -> None: ...
    last_update_success: bool
    @callback
    def _mark_unavailable(self) -> None: ...
