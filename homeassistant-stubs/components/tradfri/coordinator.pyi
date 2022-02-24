from .const import SCAN_INTERVAL as SCAN_INTERVAL
from collections.abc import Callable as Callable
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pytradfri.command import Command as Command
from pytradfri.device import Device
from pytradfri.group import Group
from typing import Any

_LOGGER: Any

class TradfriDeviceDataUpdateCoordinator(DataUpdateCoordinator[Device]):
    api: Any
    device: Any
    _exception: Any
    def __init__(self, hass: HomeAssistant, api: Callable[[Union[Command, list[Command]]], Any], device: Device) -> None: ...
    last_update_success: bool
    async def set_hub_available(self, available: bool) -> None: ...
    def _observe_update(self, device: Device) -> None: ...
    def _exception_callback(self, exc: Exception) -> None: ...
    update_interval: Any
    async def _handle_exception(self, exc: Exception) -> None: ...
    async def _async_update_data(self) -> Device: ...

class TradfriGroupDataUpdateCoordinator(DataUpdateCoordinator[Group]):
    api: Any
    group: Any
    _exception: Any
    def __init__(self, hass: HomeAssistant, api: Callable[[Union[Command, list[Command]]], Any], group: Group) -> None: ...
    last_update_success: bool
    async def set_hub_available(self, available: bool) -> None: ...
    update_interval: Any
    async def _async_update_data(self) -> Group: ...
