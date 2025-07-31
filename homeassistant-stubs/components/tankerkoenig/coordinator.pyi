from .const import CONF_STATIONS as CONF_STATIONS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiotankerkoenig import PriceInfo, Station as Station
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ID as ATTR_ID, CONF_API_KEY as CONF_API_KEY, CONF_SHOW_ON_MAP as CONF_SHOW_ON_MAP
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
type TankerkoenigConfigEntry = ConfigEntry[TankerkoenigDataUpdateCoordinator]

class TankerkoenigDataUpdateCoordinator(DataUpdateCoordinator[dict[str, PriceInfo]]):
    config_entry: TankerkoenigConfigEntry
    _selected_stations: list[str]
    stations: dict[str, Station]
    show_on_map: bool
    _tankerkoenig: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: TankerkoenigConfigEntry, update_interval: int) -> None: ...
    async def async_setup(self) -> None: ...
    async def _async_update_data(self) -> dict[str, PriceInfo]: ...
