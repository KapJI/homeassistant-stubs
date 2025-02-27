from .coordinator import PingConfigEntry as PingConfigEntry, PingUpdateCoordinator as PingUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class PingEntity(CoordinatorEntity[PingUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, config_entry: PingConfigEntry, coordinator: PingUpdateCoordinator, unique_id: str) -> None: ...
