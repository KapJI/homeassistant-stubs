from .const import DOMAIN as DOMAIN
from .coordinator import AmazonDevicesCoordinator as AmazonDevicesCoordinator
from _typeshed import Incomplete
from aioamazondevices.api import AmazonDevice as AmazonDevice
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class AmazonEntity(CoordinatorEntity[AmazonDevicesCoordinator]):
    _attr_has_entity_name: bool
    _serial_num: Incomplete
    _attr_device_info: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AmazonDevicesCoordinator, serial_num: str, description: EntityDescription) -> None: ...
    @property
    def device(self) -> AmazonDevice: ...
    @property
    def available(self) -> bool: ...
