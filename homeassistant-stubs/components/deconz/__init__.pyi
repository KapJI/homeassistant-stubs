from .config_flow import get_master_gateway as get_master_gateway
from .const import CONF_GROUP_ID_BASE as CONF_GROUP_ID_BASE, CONF_MASTER_GATEWAY as CONF_MASTER_GATEWAY, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .deconz_event import async_setup_events as async_setup_events, async_unload_events as async_unload_events
from .errors import AuthenticationRequired as AuthenticationRequired, CannotConnect as CannotConnect
from .gateway import DeconzGateway as DeconzGateway, get_deconz_session as get_deconz_session
from .services import async_setup_services as async_setup_services, async_unload_services as async_unload_services
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_update_master_gateway(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
async def async_update_group_unique_id(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
