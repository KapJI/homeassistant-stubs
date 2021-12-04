from .const import DOMAIN as DOMAIN
from .renault_entities import RenaultDataEntity as RenaultDataEntity, RenaultDataEntityDescription as RenaultDataEntityDescription
from .renault_hub import RenaultHub as RenaultHub
from homeassistant.components.device_tracker import SOURCE_TYPE_GPS as SOURCE_TYPE_GPS
from homeassistant.components.device_tracker.config_entry import TrackerEntity as TrackerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from renault_api.kamereon.models import KamereonVehicleLocationData

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RenaultDeviceTracker(RenaultDataEntity[KamereonVehicleLocationData], TrackerEntity):
    @property
    def latitude(self) -> Union[float, None]: ...
    @property
    def longitude(self) -> Union[float, None]: ...
    @property
    def source_type(self) -> str: ...

DEVICE_TRACKER_TYPES: tuple[RenaultDataEntityDescription, ...]
