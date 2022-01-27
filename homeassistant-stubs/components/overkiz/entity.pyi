from .const import DOMAIN as DOMAIN
from .coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from .executor import OverkizExecutor as OverkizExecutor
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyoverkiz.models import Device as Device
from typing import Any

class OverkizEntity(CoordinatorEntity):
    coordinator: OverkizDataUpdateCoordinator
    device_url: Any
    executor: Any
    _attr_assumed_state: Any
    _attr_available: Any
    _attr_unique_id: Any
    _attr_name: Any
    _attr_device_info: Any
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator) -> None: ...
    @property
    def device(self) -> Device: ...
    def generate_device_info(self) -> DeviceInfo: ...

class OverkizDescriptiveEntity(OverkizEntity):
    entity_description: Any
    _attr_unique_id: Any
    _attr_name: Any
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator, description: EntityDescription) -> None: ...

class OverkizDeviceClass(StrEnum):
    BATTERY: str
    DISCRETE_RSSI_LEVEL: str
    MEMORIZED_SIMPLE_VOLUME: str
    OPEN_CLOSED_PEDESTRIAN: str
    PRIORITY_LOCK_ORIGINATOR: str
    SENSOR_DEFECT: str
    SENSOR_ROOM: str
