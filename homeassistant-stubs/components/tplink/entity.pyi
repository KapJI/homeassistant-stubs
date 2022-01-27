from .const import DOMAIN as DOMAIN
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from collections.abc import Awaitable as Awaitable, Callable as Callable, Coroutine
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from kasa import SmartDevice as SmartDevice
from typing import Any, TypeVar
from typing_extensions import Concatenate as Concatenate

_T = TypeVar('_T', bound='CoordinatedTPLinkEntity')
_P: Any

def async_refresh_after(func: Callable[Concatenate[_T, _P], Awaitable[None]]) -> Callable[Concatenate[_T, _P], Coroutine[Any, Any, None]]: ...

class CoordinatedTPLinkEntity(CoordinatorEntity):
    coordinator: TPLinkDataUpdateCoordinator
    device: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, device: SmartDevice, coordinator: TPLinkDataUpdateCoordinator) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def is_on(self) -> bool: ...
