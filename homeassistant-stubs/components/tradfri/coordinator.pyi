from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass, field
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pytradfri import Gateway as Gateway
from pytradfri.api.aiocoap_api import APIFactory as APIFactory
from pytradfri.command import Command as Command
from pytradfri.device import Device
from typing import Any

SCAN_INTERVAL: int
type TradfriConfigEntry = ConfigEntry[TradfriData]

@dataclass
class TradfriData:
    factory: APIFactory
    gateway: Gateway
    api: Callable[[Command | list[Command]], Any]
    coordinator_list: list[TradfriDeviceDataUpdateCoordinator] = field(default_factory=list)

class TradfriDeviceDataUpdateCoordinator(DataUpdateCoordinator[Device]):
    config_entry: TradfriConfigEntry
    api: Incomplete
    device: Incomplete
    _exception: Exception | None
    def __init__(self, hass: HomeAssistant, config_entry: TradfriConfigEntry, api: Callable[[Command | list[Command]], Any], device: Device) -> None: ...
    last_update_success: bool
    async def set_hub_available(self, available: bool) -> None: ...
    @callback
    def _observe_update(self, device: Device) -> None: ...
    @callback
    def _exception_callback(self, exc: Exception) -> None: ...
    update_interval: Incomplete
    async def _handle_exception(self, exc: Exception) -> None: ...
    async def _async_update_data(self) -> Device: ...
