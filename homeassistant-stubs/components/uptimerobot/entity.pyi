from .const import ATTRIBUTION as ATTRIBUTION, ATTR_TARGET as ATTR_TARGET, DOMAIN as DOMAIN
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from pyuptimerobot import UptimeRobotMonitor as UptimeRobotMonitor
from typing import Any

class UptimeRobotEntity(CoordinatorEntity):
    entity_description: Any
    _monitor: Any
    _attr_device_info: Any
    _attr_extra_state_attributes: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: DataUpdateCoordinator, description: EntityDescription, monitor: UptimeRobotMonitor) -> None: ...
    @property
    def _monitors(self) -> list[UptimeRobotMonitor]: ...
    @property
    def monitor(self) -> UptimeRobotMonitor: ...
    @property
    def monitor_available(self) -> bool: ...
