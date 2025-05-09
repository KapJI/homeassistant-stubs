from .const import API_REFRESH as API_REFRESH
from _typeshed import Incomplete
from ayla_iot_unofficial import AylaApi as AylaApi
from ayla_iot_unofficial.fujitsu_hvac import FujitsuHVAC
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete
type FGLairConfigEntry = ConfigEntry[FGLairCoordinator]

class FGLairCoordinator(DataUpdateCoordinator[dict[str, FujitsuHVAC]]):
    config_entry: FGLairConfigEntry
    api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: FGLairConfigEntry, api: AylaApi) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> dict[str, FujitsuHVAC]: ...
