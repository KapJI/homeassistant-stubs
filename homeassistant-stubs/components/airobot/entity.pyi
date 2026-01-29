from .const import DOMAIN as DOMAIN
from .coordinator import AirobotDataUpdateCoordinator as AirobotDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_MAC as CONF_MAC
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class AirobotEntity(CoordinatorEntity[AirobotDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AirobotDataUpdateCoordinator) -> None: ...
