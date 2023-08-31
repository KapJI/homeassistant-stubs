from .const import DOMAIN as DOMAIN
from .coordinator import LaMetricDataUpdateCoordinator as LaMetricDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo, format_mac as format_mac
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class LaMetricEntity(CoordinatorEntity[LaMetricDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LaMetricDataUpdateCoordinator) -> None: ...
