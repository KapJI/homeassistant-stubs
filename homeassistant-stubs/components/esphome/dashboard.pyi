import aiohttp
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from esphome_dashboard_api import ConfiguredDevice
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.singleton import singleton as singleton
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete
KEY_DASHBOARD_MANAGER: str
STORAGE_KEY: str
STORAGE_VERSION: int

async def async_setup(hass: HomeAssistant) -> None: ...
async def async_get_or_create_dashboard_manager(hass: HomeAssistant) -> ESPHomeDashboardManager: ...

class ESPHomeDashboardManager:
    _hass: Incomplete
    _store: Incomplete
    _data: Incomplete
    _current_dashboard: Incomplete
    _cancel_shutdown: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_setup(self) -> None: ...
    def async_get(self) -> ESPHomeDashboard | None: ...
    async def async_set_dashboard_info(self, addon_slug: str, host: str, port: int) -> None: ...

def async_get_dashboard(hass: HomeAssistant) -> ESPHomeDashboard | None: ...
async def async_set_dashboard_info(hass: HomeAssistant, addon_slug: str, host: str, port: int) -> None: ...

class ESPHomeDashboard(DataUpdateCoordinator[dict[str, ConfiguredDevice]]):
    addon_slug: Incomplete
    url: Incomplete
    api: Incomplete
    def __init__(self, hass: HomeAssistant, addon_slug: str, url: str, session: aiohttp.ClientSession) -> None: ...
    @property
    def supports_update(self) -> bool: ...
    async def _async_update_data(self) -> dict: ...
