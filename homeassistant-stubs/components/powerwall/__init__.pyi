from .const import AUTH_COOKIE_KEY as AUTH_COOKIE_KEY, CONFIG_ENTRY_COOKIE as CONFIG_ENTRY_COOKIE, DOMAIN as DOMAIN, POWERWALL_API_CHANGED as POWERWALL_API_CHANGED, POWERWALL_COORDINATOR as POWERWALL_COORDINATOR, UPDATE_INTERVAL as UPDATE_INTERVAL
from .models import PowerwallBaseInfo as PowerwallBaseInfo, PowerwallConfigEntry as PowerwallConfigEntry, PowerwallData as PowerwallData, PowerwallRuntimeData as PowerwallRuntimeData
from _typeshed import Incomplete
from aiohttp import CookieJar
from homeassistant.components import persistent_notification as persistent_notification
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.network import is_ip_address as is_ip_address
from tesla_powerwall import Powerwall

PLATFORMS: Incomplete
_LOGGER: Incomplete
API_CHANGED_ERROR_BODY: str
API_CHANGED_TITLE: str

class PowerwallDataManager:
    hass: Incomplete
    ip_address: Incomplete
    password: Incomplete
    runtime_data: Incomplete
    power_wall: Incomplete
    cookie_jar: Incomplete
    entry: Incomplete
    def __init__(self, hass: HomeAssistant, power_wall: Powerwall, cookie_jar: CookieJar, entry: PowerwallConfigEntry, ip_address: str, password: str | None, runtime_data: PowerwallRuntimeData) -> None: ...
    @property
    def api_changed(self) -> int: ...
    async def _recreate_powerwall_login(self) -> None: ...
    async def async_update_data(self) -> PowerwallData: ...
    async def _update_data(self) -> PowerwallData: ...
    @callback
    def save_auth_cookie(self) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: PowerwallConfigEntry) -> bool: ...
async def async_migrate_entity_unique_ids(hass: HomeAssistant, entry: PowerwallConfigEntry, base_info: PowerwallBaseInfo) -> None: ...
async def _login_and_fetch_base_info(power_wall: Powerwall, host: str, password: str | None, use_auth_cookie: bool) -> PowerwallBaseInfo: ...
async def _call_base_info(power_wall: Powerwall, host: str) -> PowerwallBaseInfo: ...
async def get_backup_reserve_percentage(power_wall: Powerwall) -> float | None: ...
async def _fetch_powerwall_data(power_wall: Powerwall) -> PowerwallData: ...
@callback
def async_last_update_was_successful(hass: HomeAssistant, entry: PowerwallConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
