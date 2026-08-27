from .const import DATA_WIIM as DATA_WIIM, DOMAIN as DOMAIN, LOGGER as LOGGER, PLATFORMS as PLATFORMS, UPNP_PORT as UPNP_PORT, WiimConfigEntry as WiimConfigEntry
from .models import WiimData as WiimData
from .util import async_get_event_callback_host as async_get_event_callback_host
from homeassistant.const import CONF_HOST as CONF_HOST, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

DEFAULT_AVAILABILITY_POLLING_INTERVAL: int

async def async_setup_entry(hass: HomeAssistant, entry: WiimConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: WiimConfigEntry) -> bool: ...
