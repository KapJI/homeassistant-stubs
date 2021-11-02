from . import RitualsDataUpdateCoordinator as RitualsDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyrituals import Diffuser as Diffuser
from typing import Any

MANUFACTURER: str
MODEL: str
MODEL2: str

class DiffuserEntity(CoordinatorEntity):
    coordinator: RitualsDataUpdateCoordinator
    _diffuser: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, diffuser: Diffuser, coordinator: RitualsDataUpdateCoordinator, entity_suffix: str) -> None: ...
    @property
    def available(self) -> bool: ...
