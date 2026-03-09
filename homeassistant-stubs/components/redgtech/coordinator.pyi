from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

UPDATE_INTERVAL: Incomplete
_LOGGER: Incomplete

@dataclass
class RedgtechDevice:
    unique_id: str
    name: str
    state: bool
type RedgtechConfigEntry = ConfigEntry[RedgtechDataUpdateCoordinator]

class RedgtechDataUpdateCoordinator(DataUpdateCoordinator[dict[str, RedgtechDevice]]):
    config_entry: RedgtechConfigEntry
    api: Incomplete
    access_token: str | None
    email: Incomplete
    password: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: RedgtechConfigEntry) -> None: ...
    async def login(self, email: str, password: str) -> str | None: ...
    async def renew_token(self, email: str, password: str) -> None: ...
    async def call_api_with_valid_token[_R, *_Ts](self, api_call: Callable[[*_Ts], Coroutine[Any, Any, _R]], *args: *_Ts) -> _R: ...
    async def _async_update_data(self) -> dict[str, RedgtechDevice]: ...
