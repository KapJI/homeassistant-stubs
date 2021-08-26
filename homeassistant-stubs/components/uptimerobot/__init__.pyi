from .const import API_ATTR_OK as API_ATTR_OK, COORDINATOR_UPDATE_INTERVAL as COORDINATOR_UPDATE_INTERVAL, DOMAIN as DOMAIN, LOGGER as LOGGER, PLATFORMS as PLATFORMS
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceRegistry as DeviceRegistry, async_entries_for_config_entry as async_entries_for_config_entry, async_get_registry as async_get_registry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyuptimerobot import UptimeRobot, UptimeRobotMonitor as UptimeRobotMonitor
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class UptimeRobotDataUpdateCoordinator(DataUpdateCoordinator):
    _config_entry_id: Any
    _device_registry: Any
    _api: Any
    def __init__(self, hass: HomeAssistant, config_entry_id: str, dev_reg: DeviceRegistry, api: UptimeRobot) -> None: ...
    async def _async_update_data(self) -> Union[list[UptimeRobotMonitor], None]: ...
