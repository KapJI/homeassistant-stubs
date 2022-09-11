from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from devolo_plc_api.device import Device as Device
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

class DevoloEntity(CoordinatorEntity):
    _attr_has_entity_name: bool
    device: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, device: Device, device_name: str) -> None: ...
