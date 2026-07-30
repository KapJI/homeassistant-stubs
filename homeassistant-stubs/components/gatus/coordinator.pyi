from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from gatus_api import EndpointStatus
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

_LOGGER: Incomplete
type GatusConfigEntry = ConfigEntry[GatusDataUpdateCoordinator]

class GatusDataUpdateCoordinator(DataUpdateCoordinator[dict[str, EndpointStatus]]):
    url: Incomplete
    client: Incomplete
    _entry_id: Incomplete
    _known_endpoint_keys: Incomplete
    def __init__(self, hass: HomeAssistant, entry: GatusConfigEntry, url: str) -> None: ...
    @override
    async def _async_update_data(self) -> dict[str, EndpointStatus]: ...
