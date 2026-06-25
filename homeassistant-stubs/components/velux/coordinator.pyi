from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyvlx.opening_device import OpeningDevice as OpeningDevice, Position as Position
from typing import override

SCAN_INTERVAL: Incomplete

@dataclass
class VeluxLimitationData:
    limitation_min: Position

class VeluxLimitationCoordinator(DataUpdateCoordinator[VeluxLimitationData | None]):
    node: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, node: OpeningDevice) -> None: ...
    @override
    async def _async_update_data(self) -> VeluxLimitationData: ...
