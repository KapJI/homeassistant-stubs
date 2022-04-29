from . import RitualsDataUpdateCoordinator as RitualsDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyrituals import Diffuser as Diffuser

MANUFACTURER: str
MODEL: str
MODEL2: str

class DiffuserEntity(CoordinatorEntity[RitualsDataUpdateCoordinator]):
    _diffuser: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, diffuser: Diffuser, coordinator: RitualsDataUpdateCoordinator, entity_suffix: str) -> None: ...
    @property
    def available(self) -> bool: ...
