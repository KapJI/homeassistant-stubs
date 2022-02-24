from .const import DOMAIN as DOMAIN
from datetime import datetime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.dt import utcnow as utcnow
from rokuecp import Roku
from rokuecp.models import Device
from typing import Any

REQUEST_REFRESH_DELAY: float
SCAN_INTERVAL: Any
_LOGGER: Any

class RokuDataUpdateCoordinator(DataUpdateCoordinator[Device]):
    last_full_update: Union[datetime, None]
    roku: Roku
    full_update_interval: Any
    def __init__(self, hass: HomeAssistant, host: str) -> None: ...
    async def _async_update_data(self) -> Device: ...
