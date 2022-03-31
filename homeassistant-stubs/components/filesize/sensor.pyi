from .const import CONF_FILE_PATHS as CONF_FILE_PATHS, DOMAIN as DOMAIN
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_FILE_PATH as CONF_FILE_PATH, DATA_BYTES as DATA_BYTES, DATA_MEGABYTES as DATA_MEGABYTES
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Any
ICON: str
SENSOR_TYPES: Any
PLATFORM_SCHEMA: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FileSizeCoordinator(DataUpdateCoordinator):
    _path: Any
    def __init__(self, hass: HomeAssistant, path: str) -> None: ...
    async def _async_update_data(self) -> dict[str, Union[float, int, datetime]]: ...

class FilesizeEntity(CoordinatorEntity[FileSizeCoordinator], SensorEntity):
    entity_description: SensorEntityDescription
    _attr_name: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, description: SensorEntityDescription, path: str, entry_id: str, coordinator: FileSizeCoordinator) -> None: ...
    @property
    def native_value(self) -> Union[float, int, datetime]: ...
