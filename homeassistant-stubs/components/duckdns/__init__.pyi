from .const import ATTR_CONFIG_ENTRY as ATTR_CONFIG_ENTRY
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from collections.abc import Callable as Callable, Coroutine, Sequence
from datetime import datetime, timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_DOMAIN as CONF_DOMAIN
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.selector import ConfigEntrySelector as ConfigEntrySelector
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from typing import Any

_LOGGER: Incomplete
ATTR_TXT: str
DOMAIN: str
INTERVAL: Incomplete
BACKOFF_INTERVALS: Incomplete
SERVICE_SET_TXT: str
UPDATE_URL: str
CONFIG_SCHEMA: Incomplete
SERVICE_TXT_SCHEMA: Incomplete
type DuckDnsConfigEntry = ConfigEntry

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: DuckDnsConfigEntry) -> bool: ...
def get_config_entry(hass: HomeAssistant, entry_id: str | None = None) -> DuckDnsConfigEntry: ...
async def update_domain_service(call: ServiceCall) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: DuckDnsConfigEntry) -> bool: ...

_SENTINEL: Incomplete

async def _update_duckdns(session: ClientSession, domain: str, token: str, *, txt: str | None | object = ..., clear: bool = False) -> bool: ...
@callback
@bind_hass
def async_track_time_interval_backoff(hass: HomeAssistant, action: Callable[[datetime], Coroutine[Any, Any, bool]], intervals: Sequence[timedelta]) -> CALLBACK_TYPE: ...
