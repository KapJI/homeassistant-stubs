from .const import CONF_ALTITUDE as CONF_ALTITUDE, DEFAULT_ALTITUDE as DEFAULT_ALTITUDE, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import OpenSkyDataUpdateCoordinator as OpenSkyDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME, CONF_RADIUS as CONF_RADIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OpenSkySensor(CoordinatorEntity[OpenSkyDataUpdateCoordinator], SensorEntity):
    _attr_attribution: str
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_icon: str
    _attr_native_unit_of_measurement: str
    _attr_state_class: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: OpenSkyDataUpdateCoordinator, config_entry: ConfigEntry) -> None: ...
    @property
    def native_value(self) -> int: ...
