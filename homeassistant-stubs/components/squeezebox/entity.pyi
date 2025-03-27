from .const import DOMAIN as DOMAIN, STATUS_QUERY_UUID as STATUS_QUERY_UUID
from .coordinator import LMSStatusDataUpdateCoordinator as LMSStatusDataUpdateCoordinator, SqueezeBoxPlayerUpdateCoordinator as SqueezeBoxPlayerUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo, format_mac as format_mac
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class SqueezeboxEntity(CoordinatorEntity[SqueezeBoxPlayerUpdateCoordinator]):
    _attr_has_entity_name: bool
    _player: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SqueezeBoxPlayerUpdateCoordinator) -> None: ...

class LMSStatusEntity(CoordinatorEntity[LMSStatusDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LMSStatusDataUpdateCoordinator, description: EntityDescription) -> None: ...
