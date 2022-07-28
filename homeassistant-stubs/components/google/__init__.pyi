from .api import ApiAuthImpl as ApiAuthImpl, get_feature_access as get_feature_access
from .const import CONF_CALENDAR_ACCESS as CONF_CALENDAR_ACCESS, DATA_CONFIG as DATA_CONFIG, DATA_SERVICE as DATA_SERVICE, DEVICE_AUTH_IMPL as DEVICE_AUTH_IMPL, DOMAIN as DOMAIN, EVENT_DESCRIPTION as EVENT_DESCRIPTION, EVENT_END_DATE as EVENT_END_DATE, EVENT_END_DATETIME as EVENT_END_DATETIME, EVENT_IN as EVENT_IN, EVENT_IN_DAYS as EVENT_IN_DAYS, EVENT_IN_WEEKS as EVENT_IN_WEEKS, EVENT_START_DATE as EVENT_START_DATE, EVENT_START_DATETIME as EVENT_START_DATETIME, EVENT_SUMMARY as EVENT_SUMMARY, EVENT_TYPES_CONF as EVENT_TYPES_CONF, FeatureAccess as FeatureAccess
from _typeshed import Incomplete
from collections.abc import Mapping
from gcal_sync.api import GoogleCalendarService
from homeassistant import config_entries as config_entries
from homeassistant.components.application_credentials import ClientCredential as ClientCredential, async_import_client_credential as async_import_client_credential
from homeassistant.components.repairs import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_OFFSET as CONF_OFFSET
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity import generate_entity_id as generate_entity_id
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
ENTITY_ID_FORMAT: Incomplete
CONF_TRACK_NEW: str
CONF_CAL_ID: str
CONF_TRACK: str
CONF_SEARCH: str
CONF_IGNORE_AVAILABILITY: str
CONF_MAX_RESULTS: str
DEFAULT_CONF_OFFSET: str
EVENT_CALENDAR_ID: str
NOTIFICATION_ID: str
NOTIFICATION_TITLE: str
GROUP_NAME_ALL_CALENDARS: str
SERVICE_ADD_EVENT: str
YAML_DEVICES: Incomplete
TOKEN_FILE: Incomplete
PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete
_SINGLE_CALSEARCH_CONFIG: Incomplete
DEVICE_SCHEMA: Incomplete
_EVENT_IN_TYPES: Incomplete
ADD_EVENT_SERVICE_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def async_entry_has_scopes(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_setup_add_event_service(hass: HomeAssistant, calendar_service: GoogleCalendarService) -> None: ...
def get_calendar_info(hass: HomeAssistant, calendar: Mapping[str, Any]) -> dict[str, Any]: ...
def load_config(path: str) -> dict[str, Any]: ...
def update_config(path: str, calendar: dict[str, Any]) -> None: ...
