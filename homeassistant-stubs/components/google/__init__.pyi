from .api import ApiAuthImpl as ApiAuthImpl, get_feature_access as get_feature_access
from .const import DOMAIN as DOMAIN
from .store import GoogleConfigEntry as GoogleConfigEntry, GoogleRuntimeData as GoogleRuntimeData, LocalCalendarStore as LocalCalendarStore
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_OFFSET as CONF_OFFSET, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity import generate_entity_id as generate_entity_id
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
YAML_DEVICES: Incomplete
PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete
_SINGLE_CALSEARCH_CONFIG: Incomplete
DEVICE_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: GoogleConfigEntry) -> bool: ...
def async_entry_has_scopes(entry: GoogleConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: GoogleConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: GoogleConfigEntry) -> None: ...
def get_calendar_info(hass: HomeAssistant, calendar: Mapping[str, Any]) -> dict[str, Any]: ...
def load_config(path: str) -> dict[str, Any]: ...
def update_config(path: str, calendar: dict[str, Any]) -> None: ...
