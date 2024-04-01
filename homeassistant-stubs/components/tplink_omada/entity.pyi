from .const import DOMAIN as DOMAIN
from .coordinator import OmadaCoordinator as OmadaCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from tplink_omada_client.devices import OmadaDevice as OmadaDevice
from typing import Generic, TypeVar

T = TypeVar('T', bound='OmadaCoordinator[Any]')

class OmadaDeviceEntity(CoordinatorEntity[T], Generic[T]):
    device: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: T, device: OmadaDevice) -> None: ...
