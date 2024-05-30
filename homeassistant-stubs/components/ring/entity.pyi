from .const import ATTRIBUTION as ATTRIBUTION, DOMAIN as DOMAIN
from .coordinator import RingDataCoordinator as RingDataCoordinator, RingNotificationsCoordinator as RingNotificationsCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.core import callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from ring_doorbell import RingDevices as RingDevices, RingGeneric
from typing import Concatenate, Generic
from typing_extensions import TypeVar

RingDeviceT = TypeVar('RingDeviceT', bound=RingGeneric, default=RingGeneric)
_RingCoordinatorT = TypeVar('_RingCoordinatorT', bound=RingDataCoordinator | RingNotificationsCoordinator)

def exception_wrap(func: Callable[Concatenate[_RingBaseEntityT, _P], _R]) -> Callable[Concatenate[_RingBaseEntityT, _P], _R]: ...

class RingBaseEntity(CoordinatorEntity[_RingCoordinatorT], Generic[_RingCoordinatorT, RingDeviceT]):
    _attr_attribution = ATTRIBUTION
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _device: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, device: RingDeviceT, coordinator: _RingCoordinatorT) -> None: ...

class RingEntity(RingBaseEntity[RingDataCoordinator, RingDeviceT]):
    def _get_coordinator_data(self) -> RingDevices: ...
    _device: Incomplete
    def _handle_coordinator_update(self) -> None: ...
