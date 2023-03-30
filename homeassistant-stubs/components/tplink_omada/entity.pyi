from .const import DOMAIN as DOMAIN
from .coordinator import OmadaCoordinator as OmadaCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from tplink_omada_client.devices import OmadaDevice as OmadaDevice
from typing import TypeVar

T = TypeVar('T')

class OmadaDeviceEntity(CoordinatorEntity[OmadaCoordinator[T]]):
    device: Incomplete
    def __init__(self, coordinator: OmadaCoordinator[T], device: OmadaDevice) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
