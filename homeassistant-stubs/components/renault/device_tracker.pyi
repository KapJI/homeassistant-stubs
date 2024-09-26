from . import RenaultConfigEntry as RenaultConfigEntry
from .entity import RenaultDataEntity as RenaultDataEntity, RenaultDataEntityDescription as RenaultDataEntityDescription
from dataclasses import dataclass
from homeassistant.components.device_tracker import TrackerEntity as TrackerEntity, TrackerEntityDescription as TrackerEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from renault_api.kamereon.models import KamereonVehicleLocationData

@dataclass(frozen=True, kw_only=True)
class RenaultTrackerEntityDescription(TrackerEntityDescription, RenaultDataEntityDescription):
    def __init__(self, coordinator, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=...) -> None: ...

async def async_setup_entry(hass: HomeAssistant, config_entry: RenaultConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RenaultDeviceTracker(RenaultDataEntity[KamereonVehicleLocationData], TrackerEntity):
    entity_description: RenaultTrackerEntityDescription
    @property
    def latitude(self) -> float | None: ...
    @property
    def longitude(self) -> float | None: ...

DEVICE_TRACKER_TYPES: tuple[RenaultTrackerEntityDescription, ...]
