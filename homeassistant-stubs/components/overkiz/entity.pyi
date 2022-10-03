from .const import DOMAIN as DOMAIN
from .coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from .executor import OverkizExecutor as OverkizExecutor
from _typeshed import Incomplete
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyoverkiz.models import Device as Device

class OverkizEntity(CoordinatorEntity[OverkizDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    device_url: Incomplete
    executor: Incomplete
    _attr_assumed_state: Incomplete
    _attr_available: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator) -> None: ...
    @property
    def is_sub_device(self) -> bool: ...
    @property
    def device(self) -> Device: ...
    def generate_device_info(self) -> DeviceInfo: ...

class OverkizDescriptiveEntity(OverkizEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator, description: EntityDescription) -> None: ...

class OverkizDeviceClass(StrEnum):
    BATTERY: str
    DISCRETE_RSSI_LEVEL: str
    MEMORIZED_SIMPLE_VOLUME: str
    OPEN_CLOSED_PEDESTRIAN: str
    PRIORITY_LOCK_ORIGINATOR: str
    SENSOR_DEFECT: str
    SENSOR_ROOM: str
    THREE_WAY_HANDLE_DIRECTION: str
