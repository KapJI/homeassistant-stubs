from .const import DOMAIN as DOMAIN, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pajgps_api.models.device import Device as Device
from pajgps_api.models.trackpoint import TrackPoint as TrackPoint

_LOGGER: Incomplete
type PajGpsConfigEntry = ConfigEntry[PajGpsCoordinator]

@dataclass
class PajGpsData:
    devices: dict[int, Device]
    positions: dict[int, TrackPoint]

class PajGpsCoordinator(DataUpdateCoordinator[PajGpsData]):
    config_entry: PajGpsConfigEntry
    _email: str
    _user_id: int | None
    api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: PajGpsConfigEntry) -> None: ...
    @property
    def email(self) -> str: ...
    @property
    def user_id(self) -> int | None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> PajGpsData: ...
