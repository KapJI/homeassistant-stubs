from . import RokuDataUpdateCoordinator as RokuDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class RokuEntity(CoordinatorEntity[RokuDataUpdateCoordinator]):
    _device_id: Incomplete
    entity_description: Incomplete
    _attr_name: Incomplete
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, device_id: Union[str, None], coordinator: RokuDataUpdateCoordinator, description: Union[EntityDescription, None] = ...) -> None: ...
