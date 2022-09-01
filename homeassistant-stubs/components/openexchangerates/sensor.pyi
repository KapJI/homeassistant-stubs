from .const import DEFAULT_BASE as DEFAULT_BASE, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import OpenexchangeratesCoordinator as OpenexchangeratesCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_BASE as CONF_BASE, CONF_NAME as CONF_NAME, CONF_QUOTE as CONF_QUOTE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

ATTRIBUTION: str
DEFAULT_NAME: str

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OpenexchangeratesSensor(CoordinatorEntity[OpenexchangeratesCoordinator], SensorEntity):
    _attr_attribution: Incomplete
    _attr_device_info: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    _attr_name: Incomplete
    _attr_has_entity_name: bool
    _attr_native_unit_of_measurement: Incomplete
    _attr_unique_id: Incomplete
    _quote: Incomplete
    def __init__(self, config_entry: ConfigEntry, coordinator: OpenexchangeratesCoordinator, name: Union[str, None], quote: str, enabled: bool) -> None: ...
    @property
    def native_value(self) -> float: ...
