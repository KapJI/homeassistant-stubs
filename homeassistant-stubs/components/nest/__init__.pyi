from . import api as api, config_flow as config_flow
from .const import CONF_PROJECT_ID as CONF_PROJECT_ID, CONF_SUBSCRIBER_ID as CONF_SUBSCRIBER_ID, DATA_NEST_CONFIG as DATA_NEST_CONFIG, DATA_SDM as DATA_SDM, DATA_SUBSCRIBER as DATA_SUBSCRIBER, DOMAIN as DOMAIN, OAUTH2_AUTHORIZE as OAUTH2_AUTHORIZE, OAUTH2_TOKEN as OAUTH2_TOKEN, OOB_REDIRECT_URI as OOB_REDIRECT_URI
from .events import EVENT_NAME_MAP as EVENT_NAME_MAP, NEST_EVENT as NEST_EVENT
from .legacy import async_setup_legacy as async_setup_legacy, async_setup_legacy_entry as async_setup_legacy_entry
from .media_source import get_media_source_devices as get_media_source_devices
from aiohttp import web
from google_nest_sdm.event import EventMessage as EventMessage
from homeassistant.auth.permissions.const import POLICY_READ as POLICY_READ
from homeassistant.components.http.const import KEY_HASS_USER as KEY_HASS_USER
from homeassistant.components.http.view import HomeAssistantView as HomeAssistantView
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_MONITORED_CONDITIONS as CONF_MONITORED_CONDITIONS, CONF_SENSORS as CONF_SENSORS, CONF_STRUCTURE as CONF_STRUCTURE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError, Unauthorized as Unauthorized
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.entity_registry import async_entries_for_device as async_entries_for_device
from homeassistant.helpers.typing import ConfigType as ConfigType
from http import HTTPStatus
from typing import Any

_LOGGER: Any
DATA_NEST_UNAVAILABLE: str
NEST_SETUP_NOTIFICATION: str
SENSOR_SCHEMA: Any
CONFIG_SCHEMA: Any
PLATFORMS: Any
WEB_AUTH_DOMAIN = DOMAIN
INSTALLED_AUTH_DOMAIN: Any
EVENT_MEDIA_CACHE_SIZE: int

class WebAuth(config_entry_oauth2_flow.LocalOAuth2Implementation):
    name: str
    def __init__(self, hass: HomeAssistant, client_id: str, client_secret: str, project_id: str) -> None: ...

class InstalledAppAuth(config_entry_oauth2_flow.LocalOAuth2Implementation):
    name: str
    def __init__(self, hass: HomeAssistant, client_id: str, client_secret: str, project_id: str) -> None: ...
    @property
    def redirect_uri(self) -> str: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class SignalUpdateCallback:
    _hass: Any
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_handle_event(self, event_message: EventMessage) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...

class NestEventMediaView(HomeAssistantView):
    url: str
    name: str
    hass: Any
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def get(self, request: web.Request, device_id: str, event_id: str) -> web.StreamResponse: ...
    def _json_error(self, message: str, status: HTTPStatus) -> web.StreamResponse: ...
