from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pydroid_ipcam import PyDroidIPCam as PyDroidIPCam

_LOGGER: Incomplete

class AndroidIPCamDataUpdateCoordinator(DataUpdateCoordinator[None]):
    hass: Incomplete
    config_entry: Incomplete
    cam: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, cam: PyDroidIPCam) -> None: ...
    async def _async_update_data(self) -> None: ...
