from . import api as api, config_flow as config_flow
from .const import DATA_SDM as DATA_SDM, DATA_SUBSCRIBER as DATA_SUBSCRIBER, DOMAIN as DOMAIN, OAUTH2_AUTHORIZE as OAUTH2_AUTHORIZE, OAUTH2_TOKEN as OAUTH2_TOKEN
from .events import EVENT_NAME_MAP as EVENT_NAME_MAP, NEST_EVENT as NEST_EVENT
from .legacy import async_setup_legacy as async_setup_legacy, async_setup_legacy_entry as async_setup_legacy_entry
from google_nest_sdm.event import EventMessage as EventMessage
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_MONITORED_CONDITIONS as CONF_MONITORED_CONDITIONS, CONF_SENSORS as CONF_SENSORS, CONF_STRUCTURE as CONF_STRUCTURE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client, config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import Any

_LOGGER: Any
CONF_PROJECT_ID: str
CONF_SUBSCRIBER_ID: str
DATA_NEST_CONFIG: str
DATA_NEST_UNAVAILABLE: str
NEST_SETUP_NOTIFICATION: str
SENSOR_SCHEMA: Any
CONFIG_SCHEMA: Any
PLATFORMS: Any

async def async_setup(hass: HomeAssistant, config: dict) -> bool: ...

class SignalUpdateCallback:
    _hass: Any
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_handle_event(self, event_message: EventMessage) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
