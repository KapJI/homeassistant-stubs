from .const import DOMAIN as DOMAIN
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from kasa import SmartDevice as SmartDevice
from typing import Any, Concatenate, TypeVar

_T = TypeVar('_T', bound='CoordinatedTPLinkEntity')
_P: Incomplete

def async_refresh_after(func: Callable[Concatenate[_T, _P], Awaitable[None]]) -> Callable[Concatenate[_T, _P], Coroutine[Any, Any, None]]: ...

class CoordinatedTPLinkEntity(CoordinatorEntity[TPLinkDataUpdateCoordinator]):
    device: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: SmartDevice, coordinator: TPLinkDataUpdateCoordinator) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def is_on(self) -> bool: ...
