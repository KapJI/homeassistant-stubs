from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from linear_garage_door import Linear
from typing import Any

_LOGGER: Incomplete

class LinearUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    _email: str
    _password: str
    _device_id: str
    _site_id: str
    _devices: list[dict[str, list[str] | str]] | None
    _linear: Linear
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
