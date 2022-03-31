from . import UptimeRobotDataUpdateCoordinator as UptimeRobotDataUpdateCoordinator
from .const import ATTRIBUTION as ATTRIBUTION, ATTR_TARGET as ATTR_TARGET, DOMAIN as DOMAIN
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyuptimerobot import UptimeRobotMonitor as UptimeRobotMonitor
from typing import Any

class UptimeRobotEntity(CoordinatorEntity[UptimeRobotDataUpdateCoordinator]):
    _attr_attribution: Any
    entity_description: Any
    _monitor: Any
    _attr_device_info: Any
    _attr_extra_state_attributes: Any
    _attr_unique_id: Any
    api: Any
    def __init__(self, coordinator: UptimeRobotDataUpdateCoordinator, description: EntityDescription, monitor: UptimeRobotMonitor) -> None: ...
    @property
    def _monitors(self) -> list[UptimeRobotMonitor]: ...
    @property
    def monitor(self) -> UptimeRobotMonitor: ...
    @property
    def monitor_available(self) -> bool: ...
