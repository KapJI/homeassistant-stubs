from .const import CONF_MACHINE as CONF_MACHINE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete

class LaMarzoccoUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: ConfigEntry
    lm: Incomplete
    local_connection_configured: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def _async_update_data(self) -> None: ...
    async def _async_init_client(self) -> None: ...
    async def _async_handle_request(self, func: Callable[..., Coroutine[None, None, None]], *args: Any, **kwargs: Any) -> None: ...
