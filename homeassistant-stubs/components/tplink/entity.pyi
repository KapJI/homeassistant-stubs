from .const import DOMAIN as DOMAIN
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from kasa import SmartDevice as SmartDevice
from typing import Any, Callable, TypeVar

WrapFuncType = TypeVar('WrapFuncType', bound=Callable[..., Any])

def async_refresh_after(func: WrapFuncType) -> WrapFuncType: ...

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
