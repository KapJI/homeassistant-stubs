from .const import DOMAIN as DOMAIN, POWERWALL_API_CHANGED as POWERWALL_API_CHANGED, POWERWALL_COORDINATOR as POWERWALL_COORDINATOR, POWERWALL_HTTP_SESSION as POWERWALL_HTTP_SESSION, UPDATE_INTERVAL as UPDATE_INTERVAL
from .models import PowerwallBaseInfo as PowerwallBaseInfo, PowerwallData as PowerwallData, PowerwallRuntimeData as PowerwallRuntimeData
from _typeshed import Incomplete
from homeassistant.components import persistent_notification as persistent_notification
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.network import is_ip_address as is_ip_address
from tesla_powerwall import Powerwall

CONFIG_SCHEMA: Incomplete
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
    def __init__(self, hass: HomeAssistant, power_wall: Powerwall, ip_address: str, password: Union[str, None], runtime_data: PowerwallRuntimeData) -> None: ...
    @property
    def api_changed(self) -> int: ...
    def _recreate_powerwall_login(self) -> None: ...
    async def async_update_data(self) -> PowerwallData: ...
    def _update_data(self) -> PowerwallData: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def _login_and_fetch_base_info(power_wall: Powerwall, host: str, password: str) -> PowerwallBaseInfo: ...
def call_base_info(power_wall: Powerwall, host: str) -> PowerwallBaseInfo: ...
def _fetch_powerwall_data(power_wall: Powerwall) -> PowerwallData: ...
def async_last_update_was_successful(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
