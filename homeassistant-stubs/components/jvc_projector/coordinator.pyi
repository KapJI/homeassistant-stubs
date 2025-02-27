from .const import NAME as NAME
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from jvcprojector import JvcProjector as JvcProjector
from typing import Any

_LOGGER: Incomplete
INTERVAL_SLOW: Incomplete
INTERVAL_FAST: Incomplete
type JVCConfigEntry = ConfigEntry[JvcProjectorDataUpdateCoordinator]

class JvcProjectorDataUpdateCoordinator(DataUpdateCoordinator[dict[str, str]]):
    config_entry: JVCConfigEntry
    device: Incomplete
    unique_id: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: JVCConfigEntry, device: JvcProjector) -> None: ...
    update_interval: Incomplete
    async def _async_update_data(self) -> dict[str, Any]: ...
