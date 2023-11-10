from .const import DOMAIN as DOMAIN
from .coordinator import StarlinkData as StarlinkData
from .entity import StarlinkEntity as StarlinkEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.device_tracker import SourceType as SourceType, TrackerEntity as TrackerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

@dataclass
class StarlinkDeviceTrackerEntityDescriptionMixin:
    latitude_fn: Callable[[StarlinkData], float]
    longitude_fn: Callable[[StarlinkData], float]
    def __init__(self, latitude_fn, longitude_fn) -> None: ...

@dataclass
class StarlinkDeviceTrackerEntityDescription(EntityDescription, StarlinkDeviceTrackerEntityDescriptionMixin):
    def __init__(self, latitude_fn, longitude_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

DEVICE_TRACKERS: Incomplete

class StarlinkDeviceTrackerEntity(StarlinkEntity, TrackerEntity):
    entity_description: StarlinkDeviceTrackerEntityDescription
    @property
    def source_type(self) -> SourceType | str: ...
    @property
    def latitude(self) -> float | None: ...
    @property
    def longitude(self) -> float | None: ...
