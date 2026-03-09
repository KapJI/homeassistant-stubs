from .const import NAME as NAME
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from jvcprojector import Command as Command, JvcProjector as JvcProjector
from typing import Any

_LOGGER: Incomplete
INTERVAL_SLOW: Incomplete
INTERVAL_FAST: Incomplete
CORE_COMMANDS: tuple[type[Command], ...]
TRANSLATIONS: Incomplete
TIMEOUT_RETRIES: int
TIMEOUT_SLEEP: int
type JVCConfigEntry = ConfigEntry[JvcProjectorDataUpdateCoordinator]

class JvcProjectorDataUpdateCoordinator(DataUpdateCoordinator[dict[str, str]]):
    config_entry: JVCConfigEntry
    device: JvcProjector
    unique_id: Incomplete
    capabilities: Incomplete
    state: dict[type[Command], str]
    def __init__(self, hass: HomeAssistant, config_entry: JVCConfigEntry, device: JvcProjector) -> None: ...
    update_interval: Incomplete
    async def _async_update_data(self) -> dict[str, Any]: ...
    async def _get_device_state(self, commands: set[type[Command]]) -> dict[type[Command], str]: ...
    async def _update_command_state(self, command: type[Command], new_state: dict[type[Command], str]) -> str | None: ...
    def get_options_map(self, command: str) -> dict[str, str]: ...
    def supports(self, command: type[Command]) -> bool: ...
