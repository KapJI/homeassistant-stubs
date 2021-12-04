from .const import DOMAIN as DOMAIN
from devolo_plc_api.device import Device as Device
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

class DevoloEntity(CoordinatorEntity):
    _device: Any
    _device_name: Any
    _attr_device_info: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: DataUpdateCoordinator, device: Device, device_name: str) -> None: ...
