from .const import DOMAIN as DOMAIN, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from aioaxlevpp import AxleClient as AxleClient, GridEvent
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

_LOGGER: Incomplete
type AxleConfigEntry = ConfigEntry[AxleCoordinator]

class AxleCoordinator(DataUpdateCoordinator[GridEvent | None]):
    config_entry: AxleConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, entry: AxleConfigEntry, client: AxleClient) -> None: ...
    @override
    async def _async_update_data(self) -> GridEvent | None: ...
