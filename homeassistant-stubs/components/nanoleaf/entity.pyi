from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aionanoleaf import Nanoleaf as Nanoleaf
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

class NanoleafEntity(CoordinatorEntity[DataUpdateCoordinator[None]]):
    _nanoleaf: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, nanoleaf: Nanoleaf, coordinator: DataUpdateCoordinator[None]) -> None: ...
