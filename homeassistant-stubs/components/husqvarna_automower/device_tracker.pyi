from .const import DOMAIN as DOMAIN
from .coordinator import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from .entity import AutomowerBaseEntity as AutomowerBaseEntity
from _typeshed import Incomplete
from homeassistant.components.device_tracker import SourceType as SourceType, TrackerEntity as TrackerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AutomowerDeviceTrackerEntity(AutomowerBaseEntity, TrackerEntity):
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator) -> None: ...
    @property
    def source_type(self) -> SourceType: ...
    @property
    def latitude(self) -> float: ...
    @property
    def longitude(self) -> float: ...
