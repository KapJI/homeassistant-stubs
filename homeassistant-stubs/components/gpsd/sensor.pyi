from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, ATTR_MODE as ATTR_MODE, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
ATTR_CLIMB: str
ATTR_ELEVATION: str
ATTR_GPS_TIME: str
ATTR_SPEED: str
DEFAULT_NAME: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class GpsdSensor(SensorEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_translation_key: str
    _attr_device_class: Incomplete
    _attr_options: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    agps_thread: Incomplete
    def __init__(self, host: str, port: int, unique_id: str) -> None: ...
    @property
    def native_value(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def icon(self) -> str: ...
