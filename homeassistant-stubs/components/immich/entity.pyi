from .const import DOMAIN as DOMAIN
from .coordinator import ImmichDataUpdateCoordinator as ImmichDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class ImmichEntity(CoordinatorEntity[ImmichDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ImmichDataUpdateCoordinator) -> None: ...
