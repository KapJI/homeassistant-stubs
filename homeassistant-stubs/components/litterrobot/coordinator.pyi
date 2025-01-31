from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Generator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pylitterbot import FeederRobot, LitterRobot

_LOGGER: Incomplete
UPDATE_INTERVAL: Incomplete
type LitterRobotConfigEntry = ConfigEntry[LitterRobotDataUpdateCoordinator]

class LitterRobotDataUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: LitterRobotConfigEntry
    account: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: LitterRobotConfigEntry) -> None: ...
    async def _async_update_data(self) -> None: ...
    async def _async_setup(self) -> None: ...
    def litter_robots(self) -> Generator[LitterRobot]: ...
    def feeder_robots(self) -> Generator[FeederRobot]: ...
