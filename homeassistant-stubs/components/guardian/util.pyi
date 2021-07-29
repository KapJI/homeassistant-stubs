import asyncio
from .const import LOGGER as LOGGER
from aioguardian import Client as Client
from collections.abc import Awaitable
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any, Callable

DEFAULT_UPDATE_INTERVAL: Any

class GuardianDataUpdateCoordinator(DataUpdateCoordinator[dict]):
    _api_coro: Any
    _api_lock: Any
    _client: Any
    def __init__(self, hass: HomeAssistant, client: Client, api_name: str, api_coro: Callable[..., Awaitable], api_lock: asyncio.Lock, valve_controller_uid: str) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
