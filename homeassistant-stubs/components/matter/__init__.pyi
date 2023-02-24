import asyncio
from .adapter import MatterAdapter as MatterAdapter
from .addon import get_addon_manager as get_addon_manager
from .api import async_register_api as async_register_api
from .const import CONF_INTEGRATION_CREATED_ADDON as CONF_INTEGRATION_CREATED_ADDON, CONF_USE_ADDON as CONF_USE_ADDON, DOMAIN as DOMAIN, LOGGER as LOGGER
from .discovery import SUPPORTED_PLATFORMS as SUPPORTED_PLATFORMS
from .helpers import MatterEntryData as MatterEntryData, get_matter as get_matter, get_node_from_device_entry as get_node_from_device_entry
from homeassistant.components.hassio import AddonError as AddonError, AddonManager as AddonManager, AddonState as AddonState
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_URL as CONF_URL, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from homeassistant.helpers.service import async_register_admin_service as async_register_admin_service
from matter_server.client import MatterClient

CONNECT_TIMEOUT: int
LISTEN_READY_TIMEOUT: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def _client_listen(hass: HomeAssistant, entry: ConfigEntry, matter_client: MatterClient, init_ready: asyncio.Event) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
def _async_init_services(hass: HomeAssistant) -> None: ...
async def _async_ensure_addon_running(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
def _get_addon_manager(hass: HomeAssistant) -> AddonManager: ...
