import asyncio
from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from aioguardian import Client as Client
from collections.abc import Awaitable, Callable as Callable
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

DEFAULT_UPDATE_INTERVAL: Incomplete

class GuardianDataUpdateCoordinator(DataUpdateCoordinator[dict]):
    _api_coro: Incomplete
    _api_lock: Incomplete
    _client: Incomplete
    def __init__(self, hass: HomeAssistant, *, client: Client, api_name: str, api_coro: Callable[..., Awaitable], api_lock: asyncio.Lock, valve_controller_uid: str) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
