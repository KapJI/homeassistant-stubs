from . import RenaultConfigEntry as RenaultConfigEntry
from .entity import RenaultDataEntity as RenaultDataEntity, RenaultDataEntityDescription as RenaultDataEntityDescription
from homeassistant.components.device_tracker import SourceType as SourceType, TrackerEntity as TrackerEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from renault_api.kamereon.models import KamereonVehicleLocationData

async def async_setup_entry(hass: HomeAssistant, config_entry: RenaultConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RenaultDeviceTracker(RenaultDataEntity[KamereonVehicleLocationData], TrackerEntity):
    @property
    def latitude(self) -> float | None: ...
    @property
    def longitude(self) -> float | None: ...
    @property
    def source_type(self) -> SourceType: ...

DEVICE_TRACKER_TYPES: tuple[RenaultDataEntityDescription, ...]
