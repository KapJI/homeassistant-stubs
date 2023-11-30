from . import PingDomainData as PingDomainData
from .const import CONF_IMPORTED_BY as CONF_IMPORTED_BY, CONF_PING_COUNT as CONF_PING_COUNT, DOMAIN as DOMAIN
from .coordinator import PingUpdateCoordinator as PingUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.device_tracker import AsyncSeeCallback as AsyncSeeCallback, ScannerEntity as ScannerEntity, SourceType as SourceType
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_HOSTS as CONF_HOSTS, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

_LOGGER: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_setup_scanner(hass: HomeAssistant, config: ConfigType, async_see: AsyncSeeCallback, discovery_info: DiscoveryInfoType | None = ...) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PingDeviceTracker(CoordinatorEntity[PingUpdateCoordinator], ScannerEntity):
    _attr_name: Incomplete
    config_entry: Incomplete
    def __init__(self, config_entry: ConfigEntry, coordinator: PingUpdateCoordinator) -> None: ...
    @property
    def ip_address(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def source_type(self) -> SourceType: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
