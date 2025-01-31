from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, NAME as NAME
from .coordinator import HabiticaDataUpdateCoordinator as HabiticaDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_URL as CONF_URL
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class HabiticaBase(CoordinatorEntity[HabiticaDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: HabiticaDataUpdateCoordinator, entity_description: EntityDescription) -> None: ...
