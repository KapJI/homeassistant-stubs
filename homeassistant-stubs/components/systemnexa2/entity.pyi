from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import SystemNexa2DataUpdateCoordinator as SystemNexa2DataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class SystemNexa2Entity(CoordinatorEntity[SystemNexa2DataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SystemNexa2DataUpdateCoordinator, key: str) -> None: ...
