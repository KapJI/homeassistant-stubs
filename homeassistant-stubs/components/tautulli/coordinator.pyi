from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pytautulli import PyTautulli as PyTautulli, PyTautulliApiActivity as PyTautulliApiActivity, PyTautulliApiHomeStats as PyTautulliApiHomeStats, PyTautulliApiUser as PyTautulliApiUser
from typing import Any

class TautulliDataUpdateCoordinator(DataUpdateCoordinator):
    api_client: Any
    activity: Any
    home_stats: Any
    users: Any
    def __init__(self, hass: HomeAssistant, api_client: PyTautulli) -> None: ...
    async def _async_update_data(self) -> None: ...
