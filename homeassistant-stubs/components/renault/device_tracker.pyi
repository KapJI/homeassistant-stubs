from .const import DOMAIN as DOMAIN
from .entity import RenaultDataEntity as RenaultDataEntity, RenaultDataEntityDescription as RenaultDataEntityDescription
from .renault_hub import RenaultHub as RenaultHub
from homeassistant.components.device_tracker import SourceType as SourceType, TrackerEntity as TrackerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from renault_api.kamereon.models import KamereonVehicleLocationData

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RenaultDeviceTracker(RenaultDataEntity[KamereonVehicleLocationData], TrackerEntity):
    @property
    def latitude(self) -> float | None: ...
    @property
    def longitude(self) -> float | None: ...
    @property
    def source_type(self) -> SourceType: ...

DEVICE_TRACKER_TYPES: tuple[RenaultDataEntityDescription, ...]
