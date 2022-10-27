from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .coordinator import DiskSpaceDataUpdateCoordinator as DiskSpaceDataUpdateCoordinator, HealthDataUpdateCoordinator as HealthDataUpdateCoordinator, MoviesDataUpdateCoordinator as MoviesDataUpdateCoordinator, RadarrDataUpdateCoordinator as RadarrDataUpdateCoordinator, StatusDataUpdateCoordinator as StatusDataUpdateCoordinator, T as T
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_SW_VERSION as ATTR_SW_VERSION, CONF_API_KEY as CONF_API_KEY, CONF_PLATFORM as CONF_PLATFORM, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityDescription as EntityDescription
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PLATFORMS: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class RadarrEntity(CoordinatorEntity[RadarrDataUpdateCoordinator[T]]):
    _attr_has_entity_name: bool
    coordinator: RadarrDataUpdateCoordinator[T]
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: RadarrDataUpdateCoordinator[T], description: EntityDescription) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
