import abc
from .coordinator import DormakabaDkeyCoordinator as DormakabaDkeyCoordinator
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from py_dormakaba_dkey.commands import Notifications as Notifications
from typing import override

class DormakabaDkeyEntity(CoordinatorEntity[DormakabaDkeyCoordinator], metaclass=abc.ABCMeta):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: DormakabaDkeyCoordinator) -> None: ...
    @abc.abstractmethod
    @callback
    def _async_update_attrs(self) -> None: ...
    @callback
    @override
    def _handle_coordinator_update(self) -> None: ...
    @callback
    def _handle_state_update(self, update: Notifications) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
