from .const import DOMAIN as DOMAIN
from .coordinator import LIFXSensorUpdateCoordinator as LIFXSensorUpdateCoordinator, LIFXUpdateCoordinator as LIFXUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class LIFXEntity(CoordinatorEntity[LIFXUpdateCoordinator]):
    bulb: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LIFXUpdateCoordinator) -> None: ...

class LIFXSensorEntity(CoordinatorEntity[LIFXSensorUpdateCoordinator]):
    bulb: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LIFXSensorUpdateCoordinator) -> None: ...
