from . import AsekoDataUpdateCoordinator as AsekoDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioaseko import Unit as Unit
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class AsekoEntity(CoordinatorEntity[AsekoDataUpdateCoordinator]):
    _unit: Incomplete
    _device_model: Incomplete
    _device_name: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, unit: Unit, coordinator: AsekoDataUpdateCoordinator) -> None: ...
