from . import AsekoDataUpdateCoordinator as AsekoDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from aioaseko import Unit as Unit
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class AsekoEntity(CoordinatorEntity):
    coordinator: AsekoDataUpdateCoordinator
    _unit: Any
    _device_model: Any
    _device_name: Any
    _attr_device_info: Any
    def __init__(self, unit: Unit, coordinator: AsekoDataUpdateCoordinator) -> None: ...
