from .const import DOMAIN as DOMAIN
from aionanoleaf import Nanoleaf as Nanoleaf
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

class NanoleafEntity(CoordinatorEntity):
    _nanoleaf: Any
    _attr_device_info: Any
    def __init__(self, nanoleaf: Nanoleaf, coordinator: DataUpdateCoordinator) -> None: ...
