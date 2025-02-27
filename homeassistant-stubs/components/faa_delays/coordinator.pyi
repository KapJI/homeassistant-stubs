from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from faadelays import Airport
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
type FAAConfigEntry = ConfigEntry[FAADataUpdateCoordinator]

class FAADataUpdateCoordinator(DataUpdateCoordinator[Airport]):
    session: Incomplete
    data: Incomplete
    def __init__(self, hass: HomeAssistant, entry: FAAConfigEntry, code: str) -> None: ...
    async def _async_update_data(self) -> Airport: ...
