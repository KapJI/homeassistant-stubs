from .const import DOMAIN as DOMAIN
from .coordinator import BringBaseCoordinator as BringBaseCoordinator
from _typeshed import Incomplete
from bring_api import BringList as BringList
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class BringBaseEntity(CoordinatorEntity[BringBaseCoordinator]):
    _attr_has_entity_name: bool
    _list_uuid: Incomplete
    device_info: Incomplete
    def __init__(self, coordinator: BringBaseCoordinator, bring_list: BringList) -> None: ...
