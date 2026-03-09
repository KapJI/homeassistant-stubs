from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Final

_LOGGER: Incomplete
SCAN_INTERVAL: Final[Incomplete]
type HDFuryConfigEntry = ConfigEntry[HDFuryCoordinator]

@dataclass(kw_only=True, frozen=True)
class HDFuryData:
    board: dict[str, str]
    info: dict[str, str]
    config: dict[str, str]

class HDFuryCoordinator(DataUpdateCoordinator[HDFuryData]):
    host: str
    client: Incomplete
    def __init__(self, hass: HomeAssistant, entry: HDFuryConfigEntry) -> None: ...
    async def _async_update_data(self) -> HDFuryData: ...
