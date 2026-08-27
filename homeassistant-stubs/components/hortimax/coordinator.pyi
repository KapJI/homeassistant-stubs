from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, MANUFACTURER as MANUFACTURER, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from aiohortos import Device as Device, HortosClient as HortosClient, Readout as Readout
from dataclasses import dataclass, field
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

type HortimaxConfigEntry = ConfigEntry[HortimaxCoordinator]
def source_key(source_type: str, source_name: str) -> str: ...
def readout_key(source_type: str, source_name: str, identifier: str) -> str: ...

@dataclass
class HortimaxDeviceData:
    device: Device
    readouts: dict[str, Readout] = field(default_factory=dict)
    source_names: dict[str, str] = field(default_factory=dict)

class HortimaxCoordinator(DataUpdateCoordinator[dict[str, HortimaxDeviceData]]):
    config_entry: HortimaxConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: HortimaxConfigEntry, client: HortosClient) -> None: ...
    @override
    async def _async_update_data(self) -> dict[str, HortimaxDeviceData]: ...
    @callback
    def _register_controllers(self, devices: list[Device]) -> None: ...
    @callback
    def _rename_changed_sources(self, device_id: str, device_data: HortimaxDeviceData) -> None: ...
