from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from pylitterbot import Account
from typing import Any

_LOGGER: Incomplete
UPDATE_INTERVAL_SECONDS: int

class LitterRobotHub:
    account: Account
    _data: Incomplete
    coordinator: Incomplete
    def __init__(self, hass: HomeAssistant, data: Mapping[str, Any]): ...
    async def login(self, load_robots: bool = ...) -> None: ...
