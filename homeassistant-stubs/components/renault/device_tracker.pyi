from . import RenaultConfigEntry as RenaultConfigEntry
from .entity import RenaultDataEntity as RenaultDataEntity, RenaultDataEntityDescription as RenaultDataEntityDescription
from dataclasses import dataclass
from homeassistant.components.device_tracker import TrackerEntity as TrackerEntity, TrackerEntityDescription as TrackerEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from renault_api.kamereon.models import KamereonVehicleLocationData
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RenaultTrackerEntityDescription(TrackerEntityDescription, RenaultDataEntityDescription): ...

async def async_setup_entry(hass: HomeAssistant, config_entry: RenaultConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RenaultDeviceTracker(RenaultDataEntity[KamereonVehicleLocationData], TrackerEntity):
    entity_description: RenaultTrackerEntityDescription
    @property
    @override
    def latitude(self) -> float | None: ...
    @property
    @override
    def longitude(self) -> float | None: ...

DEVICE_TRACKER_TYPES: tuple[RenaultTrackerEntityDescription, ...]
