from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Generator, Mapping
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from pylitterbot import FeederRobot, LitterRobot
from typing import Any

_LOGGER: Incomplete
UPDATE_INTERVAL_SECONDS: Incomplete

class LitterRobotHub:
    _data: Incomplete
    account: Incomplete
    coordinator: Incomplete
    def __init__(self, hass: HomeAssistant, data: Mapping[str, Any]): ...
    async def login(self, load_robots: bool = ..., subscribe_for_updates: bool = ...) -> None: ...
    def litter_robots(self) -> Generator[LitterRobot, Any, Any]: ...
    def feeder_robots(self) -> Generator[FeederRobot, Any, Any]: ...
