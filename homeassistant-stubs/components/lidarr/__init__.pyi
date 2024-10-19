from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .coordinator import DiskSpaceDataUpdateCoordinator as DiskSpaceDataUpdateCoordinator, QueueDataUpdateCoordinator as QueueDataUpdateCoordinator, StatusDataUpdateCoordinator as StatusDataUpdateCoordinator, WantedDataUpdateCoordinator as WantedDataUpdateCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType

PLATFORMS: Incomplete

@dataclass(kw_only=True, slots=True)
class LidarrData:
    disk_space: DiskSpaceDataUpdateCoordinator
    queue: QueueDataUpdateCoordinator
    status: StatusDataUpdateCoordinator
    wanted: WantedDataUpdateCoordinator
    def __init__(self, *, disk_space, queue, status, wanted) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: LidarrConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LidarrConfigEntry) -> bool: ...
