import abc
from .const import DOMAIN as DOMAIN
from .coordinator import TradfriDeviceDataUpdateCoordinator as TradfriDeviceDataUpdateCoordinator
from abc import abstractmethod
from collections.abc import Callable as Callable
from homeassistant.core import callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pytradfri.command import Command as Command
from pytradfri.device import Device as Device
from typing import Any

_LOGGER: Any

def handle_error(func: Callable[[Union[Command, list[Command]]], Any]) -> Callable[[str], Any]: ...

class TradfriBaseEntity(CoordinatorEntity, metaclass=abc.ABCMeta):
    coordinator: TradfriDeviceDataUpdateCoordinator
    _gateway_id: Any
    _device: Any
    _device_id: Any
    _api: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, device_coordinator: TradfriDeviceDataUpdateCoordinator, gateway_id: str, api: Callable[[Union[Command, list[Command]]], Any]) -> None: ...
    @abstractmethod
    def _refresh(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def available(self) -> bool: ...
