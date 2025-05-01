from .const import API_ATTR_OK as API_ATTR_OK, COORDINATOR_UPDATE_INTERVAL as COORDINATOR_UPDATE_INTERVAL, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyuptimerobot import UptimeRobot as UptimeRobot, UptimeRobotMonitor

type UptimeRobotConfigEntry = ConfigEntry[UptimeRobotDataUpdateCoordinator]
class UptimeRobotDataUpdateCoordinator(DataUpdateCoordinator[list[UptimeRobotMonitor]]):
    config_entry: UptimeRobotConfigEntry
    _device_registry: Incomplete
    api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: UptimeRobotConfigEntry, api: UptimeRobot) -> None: ...
    async def _async_update_data(self) -> list[UptimeRobotMonitor]: ...
