from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_FILE_PATH as CONF_FILE_PATH, DATA_BYTES as DATA_BYTES, DATA_MEGABYTES as DATA_MEGABYTES
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
ICON: str
SENSOR_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FileSizeCoordinator(DataUpdateCoordinator):
    _path: Incomplete
    def __init__(self, hass: HomeAssistant, path: str) -> None: ...
    async def _async_update_data(self) -> dict[str, Union[float, int, datetime]]: ...

class FilesizeEntity(CoordinatorEntity[FileSizeCoordinator], SensorEntity):
    entity_description: SensorEntityDescription
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, description: SensorEntityDescription, path: str, entry_id: str, coordinator: FileSizeCoordinator) -> None: ...
    @property
    def native_value(self) -> Union[float, int, datetime]: ...
