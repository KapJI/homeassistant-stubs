from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .coordinator import CalendarUpdateCoordinator as CalendarUpdateCoordinator, DiskSpaceDataUpdateCoordinator as DiskSpaceDataUpdateCoordinator, HealthDataUpdateCoordinator as HealthDataUpdateCoordinator, MoviesDataUpdateCoordinator as MoviesDataUpdateCoordinator, QueueDataUpdateCoordinator as QueueDataUpdateCoordinator, RadarrDataUpdateCoordinator as RadarrDataUpdateCoordinator, StatusDataUpdateCoordinator as StatusDataUpdateCoordinator, T as T
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_SW_VERSION as ATTR_SW_VERSION, CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PLATFORMS: Incomplete
RadarrConfigEntry = ConfigEntry[RadarrData]

@dataclass(kw_only=True, slots=True)
class RadarrData:
    calendar: CalendarUpdateCoordinator
    disk_space: DiskSpaceDataUpdateCoordinator
    health: HealthDataUpdateCoordinator
    movie: MoviesDataUpdateCoordinator
    queue: QueueDataUpdateCoordinator
    status: StatusDataUpdateCoordinator
    def __init__(self, *, calendar, disk_space, health, movie, queue, status) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: RadarrConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: RadarrConfigEntry) -> bool: ...

class RadarrEntity(CoordinatorEntity[RadarrDataUpdateCoordinator[T]]):
    _attr_has_entity_name: bool
    coordinator: RadarrDataUpdateCoordinator[T]
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: RadarrDataUpdateCoordinator[T], description: EntityDescription) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
