from .const import DOMAIN as DOMAIN
from .coordinator import FullyKioskDataUpdateCoordinator as FullyKioskDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class FullyKioskEntity(CoordinatorEntity[FullyKioskDataUpdateCoordinator], Entity):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: FullyKioskDataUpdateCoordinator) -> None: ...
