from .const import CONF_LOCATION as CONF_LOCATION, DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pytrafikverket.trafikverket_camera import CameraInfo as CameraInfo

_LOGGER: Incomplete
TIME_BETWEEN_UPDATES: Incomplete

@dataclass
class CameraData:
    data: CameraInfo
    image: bytes | None
    def __init__(self, data, image) -> None: ...

class TVDataUpdateCoordinator(DataUpdateCoordinator[CameraData]):
    session: Incomplete
    _camera_api: Incomplete
    _location: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> CameraData: ...
