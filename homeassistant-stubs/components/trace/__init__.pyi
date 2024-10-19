from . import websocket_api as websocket_api
from .const import CONF_STORED_TRACES as CONF_STORED_TRACES, DATA_TRACE as DATA_TRACE, DATA_TRACES_RESTORED as DATA_TRACES_RESTORED, DATA_TRACE_STORE as DATA_TRACE_STORE, DEFAULT_STORED_TRACES as DEFAULT_STORED_TRACES
from .models import ActionTrace as ActionTrace, BaseTrace as BaseTrace, RestoredTrace as RestoredTrace
from _typeshed import Incomplete
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.json import ExtendedJSONEncoder as ExtendedJSONEncoder
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.limited_size_dict import LimitedSizeDict as LimitedSizeDict
from typing import Any

_LOGGER: Incomplete
DOMAIN: str
STORAGE_KEY: str
STORAGE_VERSION: int
TRACE_CONFIG_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_get_trace(hass: HomeAssistant, key: str, run_id: str) -> dict[str, BaseTrace]: ...
async def async_list_contexts(hass: HomeAssistant, key: str | None) -> dict[str, dict[str, str]]: ...
def _get_debug_traces(hass: HomeAssistant, key: str) -> list[dict[str, Any]]: ...
async def async_list_traces(hass: HomeAssistant, wanted_domain: str, wanted_key: str | None) -> list[dict[str, Any]]: ...
def async_store_trace(hass: HomeAssistant, trace: ActionTrace, stored_traces: int) -> None: ...
def _async_store_restored_trace(hass: HomeAssistant, trace: RestoredTrace) -> None: ...
async def async_restore_traces(hass: HomeAssistant) -> None: ...
