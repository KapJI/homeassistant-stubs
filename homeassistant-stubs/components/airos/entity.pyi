from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, SECTION_ADVANCED_SETTINGS as SECTION_ADVANCED_SETTINGS
from .coordinator import AirOSDataUpdateCoordinator as AirOSDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_SSL as CONF_SSL
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class AirOSEntity(CoordinatorEntity[AirOSDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AirOSDataUpdateCoordinator) -> None: ...
