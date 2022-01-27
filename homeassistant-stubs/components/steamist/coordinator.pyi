from aiosteamist import Steamist as Steamist, SteamistStatus
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

_LOGGER: Any

class SteamistDataUpdateCoordinator(DataUpdateCoordinator[SteamistStatus]):
    client: Any
    device_name: Any
    def __init__(self, hass: HomeAssistant, client: Steamist, host: str, device_name: Union[str, None]) -> None: ...
    async def _async_update_data(self) -> SteamistStatus: ...
