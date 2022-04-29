import abc
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import TradfriDeviceDataUpdateCoordinator as TradfriDeviceDataUpdateCoordinator
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Callable as Callable
from homeassistant.core import callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pytradfri.command import Command as Command
from pytradfri.device import Device as Device
from typing import Any

def handle_error(func: Callable[[Union[Command, list[Command]]], Any]) -> Callable[[str], Any]: ...

class TradfriBaseEntity(CoordinatorEntity[TradfriDeviceDataUpdateCoordinator], metaclass=abc.ABCMeta):
    _gateway_id: Incomplete
    _device: Incomplete
    _device_id: Incomplete
    _api: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device_coordinator: TradfriDeviceDataUpdateCoordinator, gateway_id: str, api: Callable[[Union[Command, list[Command]]], Any]) -> None: ...
    @abstractmethod
    def _refresh(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def available(self) -> bool: ...
