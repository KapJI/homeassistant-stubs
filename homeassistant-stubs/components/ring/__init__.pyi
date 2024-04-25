from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import RingDataCoordinator as RingDataCoordinator, RingNotificationsCoordinator as RingNotificationsCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import APPLICATION_NAME as APPLICATION_NAME, CONF_TOKEN as CONF_TOKEN, __version__ as __version__
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from ring_doorbell import Ring, RingDevices as RingDevices

_LOGGER: Incomplete

@dataclass
class RingData:
    api: Ring
    devices: RingDevices
    devices_coordinator: RingDataCoordinator
    notifications_coordinator: RingNotificationsCoordinator
    def __init__(self, api, devices, devices_coordinator, notifications_coordinator) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
async def _migrate_old_unique_ids(hass: HomeAssistant, entry_id: str) -> None: ...
