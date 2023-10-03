from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete

class FileSizeCoordinator(DataUpdateCoordinator[dict[str, int | float | datetime]]):
    _path: Incomplete
    def __init__(self, hass: HomeAssistant, path: str) -> None: ...
    async def _async_update_data(self) -> dict[str, float | int | datetime]: ...
