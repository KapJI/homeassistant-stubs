from . import api as api
from .const import AUTH as AUTH, CONF_CLOUDHOOK_URL as CONF_CLOUDHOOK_URL, DATA_CAMERAS as DATA_CAMERAS, DATA_DEVICE_IDS as DATA_DEVICE_IDS, DATA_EVENTS as DATA_EVENTS, DATA_HANDLER as DATA_HANDLER, DATA_HOMES as DATA_HOMES, DATA_PERSONS as DATA_PERSONS, DATA_SCHEDULES as DATA_SCHEDULES, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS, WEBHOOK_DEACTIVATION as WEBHOOK_DEACTIVATION, WEBHOOK_PUSH_TYPE as WEBHOOK_PUSH_TYPE
from .data_handler import NetatmoDataHandler as NetatmoDataHandler
from .webhook import async_handle_webhook as async_handle_webhook
from _typeshed import Incomplete
from homeassistant.components import cloud as cloud
from homeassistant.components.application_credentials import ClientCredential as ClientCredential, async_import_client_credential as async_import_client_credential
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_WEBHOOK_ID as CONF_WEBHOOK_ID, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import CoreState as CoreState, Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client, config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
MAX_WEBHOOK_RETRIES: int

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_cloudhook_generate_url(hass: HomeAssistant, entry: ConfigEntry) -> str: ...
async def async_config_entry_updated(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
