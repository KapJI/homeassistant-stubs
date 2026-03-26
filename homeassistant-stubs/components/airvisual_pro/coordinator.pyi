import asyncio
from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyairvisual.node import NodeSamba as NodeSamba
from typing import Any

UPDATE_INTERVAL: Incomplete

@dataclass
class AirVisualProData:
    coordinator: AirVisualProCoordinator
    node: NodeSamba
type AirVisualProConfigEntry = ConfigEntry[AirVisualProData]

class AirVisualProCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: AirVisualProConfigEntry
    _node: Incomplete
    reload_task: asyncio.Task[bool] | None
    def __init__(self, hass: HomeAssistant, config_entry: AirVisualProConfigEntry, node: NodeSamba) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
