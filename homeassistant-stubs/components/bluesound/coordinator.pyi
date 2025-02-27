import asyncio
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from pyblu import Input as Input, Player as Player, Preset as Preset, Status as Status, SyncStatus as SyncStatus

_LOGGER: Incomplete
NODE_OFFLINE_CHECK_TIMEOUT: Incomplete
PRESET_AND_INPUTS_INTERVAL: Incomplete

@dataclass
class BluesoundRuntimeData:
    player: Player
    sync_status: SyncStatus
    coordinator: BluesoundCoordinator

@dataclass
class BluesoundData:
    sync_status: SyncStatus
    status: Status
    presets: list[Preset]
    inputs: list[Input]
type BluesoundConfigEntry = ConfigEntry[BluesoundRuntimeData]

def cancel_task(task: asyncio.Task) -> Callable[[], Coroutine[None, None, None]]: ...

class BluesoundCoordinator(DataUpdateCoordinator[BluesoundData]):
    config_entry: BluesoundConfigEntry
    player: Incomplete
    _inital_sync_status: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: BluesoundConfigEntry, player: Player, sync_status: SyncStatus) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> BluesoundData: ...
    async def _poll_presets_and_inputs_loop(self) -> None: ...
    async def _poll_status_loop(self) -> None: ...
    async def _poll_sync_status_loop(self) -> None: ...
