from .const import DOMAIN as DOMAIN
from .coordinator import MikrotikDataUpdateCoordinator as MikrotikDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class MikrotikEntity[DescriptionT: EntityDescription](CoordinatorEntity[MikrotikDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: DescriptionT
    _serial: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: MikrotikDataUpdateCoordinator, description: DescriptionT) -> None: ...
