from .const import DOMAIN as DOMAIN
from .coordinator import GeocachingDataUpdateCoordinator as GeocachingDataUpdateCoordinator
from _typeshed import Incomplete
from geocachingapi.models import GeocachingCache as GeocachingCache
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class GeocachingBaseEntity(CoordinatorEntity[GeocachingDataUpdateCoordinator]):
    _attr_has_entity_name: bool

class GeocachingCacheEntity(GeocachingBaseEntity):
    cache: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: GeocachingDataUpdateCoordinator, cache: GeocachingCache) -> None: ...
