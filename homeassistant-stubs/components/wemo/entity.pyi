from .wemo_device import DeviceCoordinator as DeviceCoordinator
from _typeshed import Incomplete
from collections.abc import Generator
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

_LOGGER: Incomplete

class WemoEntity(CoordinatorEntity[DeviceCoordinator]):
    _name_suffix: Union[str, None]
    _unique_id_suffix: Union[str, None]
    wemo: Incomplete
    _device_info: Incomplete
    def __init__(self, coordinator: DeviceCoordinator) -> None: ...
    @property
    def name_suffix(self) -> Union[str, None]: ...
    @property
    def name(self) -> str: ...
    @property
    def unique_id_suffix(self) -> Union[str, None]: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    def _wemo_call_wrapper(self, message: str) -> Generator[None, None, None]: ...

class WemoBinaryStateEntity(WemoEntity):
    @property
    def is_on(self) -> bool: ...
