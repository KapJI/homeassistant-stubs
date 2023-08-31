from .const import DOMAIN as DOMAIN
from .coordinator import SwitchBeeCoordinator as SwitchBeeCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from switchbee.device import SwitchBeeBaseDevice
from typing import Generic, TypeVar

_DeviceTypeT = TypeVar('_DeviceTypeT', bound=SwitchBeeBaseDevice)
_LOGGER: Incomplete

class SwitchBeeEntity(CoordinatorEntity[SwitchBeeCoordinator], Generic[_DeviceTypeT]):
    _attr_has_entity_name: bool
    _device: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: _DeviceTypeT, coordinator: SwitchBeeCoordinator) -> None: ...

class SwitchBeeDeviceEntity(SwitchBeeEntity[_DeviceTypeT]):
    _is_online: bool
    _attr_device_info: Incomplete
    def __init__(self, device: _DeviceTypeT, coordinator: SwitchBeeCoordinator) -> None: ...
    @property
    def available(self) -> bool: ...
    def _check_if_became_offline(self) -> None: ...
    def _check_if_became_online(self) -> None: ...
    def _get_coordinator_device(self) -> _DeviceTypeT: ...
