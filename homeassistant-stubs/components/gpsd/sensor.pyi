from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from gps3.agps3threaded import AGPS3mechanism
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, ATTR_MODE as ATTR_MODE, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, EntityCategory as EntityCategory
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
_MODE_VALUES: Incomplete

@dataclass(frozen=True, kw_only=True)
class GpsdSensorDescription(SensorEntityDescription):
    value_fn: Callable[[AGPS3mechanism], str | None]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn) -> None: ...

SENSOR_TYPES: tuple[GpsdSensorDescription, ...]
PLATFORM_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class GpsdSensor(SensorEntity):
    _attr_has_entity_name: bool
    entity_description: GpsdSensorDescription
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    agps_thread: Incomplete
    def __init__(self, host: str, port: int, unique_id: str, description: GpsdSensorDescription) -> None: ...
    @property
    def native_value(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
