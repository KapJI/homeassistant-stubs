import aiohttp
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from esphome_dashboard_api import ConfiguredDevice
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

KEY_DASHBOARD: str

def async_get_dashboard(hass: HomeAssistant) -> Union[ESPHomeDashboard, None]: ...
async def async_set_dashboard_info(hass: HomeAssistant, addon_slug: str, host: str, port: int) -> None: ...

class ESPHomeDashboard(DataUpdateCoordinator[dict[str, ConfiguredDevice]]):
    addon_slug: Incomplete
    url: Incomplete
    api: Incomplete
    def __init__(self, hass: HomeAssistant, addon_slug: str, url: str, session: aiohttp.ClientSession) -> None: ...
    @property
    def supports_update(self) -> bool: ...
    async def _async_update_data(self) -> dict: ...
