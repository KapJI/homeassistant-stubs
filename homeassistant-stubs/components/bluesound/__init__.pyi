from .const import ATTR_MASTER as ATTR_MASTER, DOMAIN as DOMAIN, SERVICE_CLEAR_TIMER as SERVICE_CLEAR_TIMER, SERVICE_JOIN as SERVICE_JOIN, SERVICE_SET_TIMER as SERVICE_SET_TIMER, SERVICE_UNJOIN as SERVICE_UNJOIN
from .coordinator import BluesoundConfigEntry as BluesoundConfigEntry, BluesoundCoordinator as BluesoundCoordinator, BluesoundRuntimeData as BluesoundRuntimeData
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import service as service
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: BluesoundConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
