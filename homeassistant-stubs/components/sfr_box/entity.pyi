from .const import DOMAIN as DOMAIN
from .coordinator import SFRDataUpdateCoordinator as SFRDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from sfrbox_api.models import SystemInfo as SystemInfo

class SFREntity(Entity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, description: EntityDescription, system_info: SystemInfo) -> None: ...

class SFRCoordinatorEntity[_T](CoordinatorEntity[SFRDataUpdateCoordinator[_T]], SFREntity):
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SFRDataUpdateCoordinator[_T], description: EntityDescription, system_info: SystemInfo) -> None: ...
