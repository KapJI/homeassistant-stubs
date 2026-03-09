from .const import ATTR_DISKS as ATTR_DISKS, ATTR_ENTRY_ID as ATTR_ENTRY_ID, ATTR_EPISODES as ATTR_EPISODES, ATTR_SHOWS as ATTR_SHOWS, DEFAULT_UPCOMING_DAYS as DEFAULT_UPCOMING_DAYS, DOMAIN as DOMAIN, SERVICE_GET_DISKSPACE as SERVICE_GET_DISKSPACE, SERVICE_GET_EPISODES as SERVICE_GET_EPISODES, SERVICE_GET_QUEUE as SERVICE_GET_QUEUE, SERVICE_GET_SERIES as SERVICE_GET_SERIES, SERVICE_GET_UPCOMING as SERVICE_GET_UPCOMING, SERVICE_GET_WANTED as SERVICE_GET_WANTED
from .coordinator import SonarrConfigEntry as SonarrConfigEntry
from .helpers import format_diskspace as format_diskspace, format_episodes as format_episodes, format_queue as format_queue, format_series as format_series, format_upcoming as format_upcoming, format_wanted as format_wanted
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import selector as selector
from typing import Any

CONF_DAYS: str
CONF_MAX_ITEMS: str
CONF_SERIES_ID: str
CONF_SEASON_NUMBER: str
CONF_SPACE_UNIT: str
SPACE_UNITS: Incomplete
DEFAULT_SPACE_UNIT: str
DEFAULT_MAX_ITEMS: int
SERVICE_BASE_SCHEMA: Incomplete
SERVICE_GET_SERIES_SCHEMA = SERVICE_BASE_SCHEMA
SERVICE_GET_EPISODES_SCHEMA: Incomplete
SERVICE_GET_QUEUE_SCHEMA: Incomplete
SERVICE_GET_DISKSPACE_SCHEMA: Incomplete
SERVICE_GET_UPCOMING_SCHEMA: Incomplete
SERVICE_GET_WANTED_SCHEMA: Incomplete

def _get_config_entry_from_service_data(call: ServiceCall) -> SonarrConfigEntry: ...
async def _handle_api_errors[_T](func: Callable[[], Awaitable[_T]]) -> _T: ...
async def _async_get_series(service: ServiceCall) -> dict[str, Any]: ...
async def _async_get_episodes(service: ServiceCall) -> dict[str, Any]: ...
async def _async_get_queue(service: ServiceCall) -> dict[str, Any]: ...
async def _async_get_diskspace(service: ServiceCall) -> dict[str, Any]: ...
async def _async_get_upcoming(service: ServiceCall) -> dict[str, Any]: ...
async def _async_get_wanted(service: ServiceCall) -> dict[str, Any]: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
