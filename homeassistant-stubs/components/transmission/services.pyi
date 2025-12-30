from .const import ATTR_DELETE_DATA as ATTR_DELETE_DATA, ATTR_DOWNLOAD_PATH as ATTR_DOWNLOAD_PATH, ATTR_LABELS as ATTR_LABELS, ATTR_TORRENT as ATTR_TORRENT, ATTR_TORRENTS as ATTR_TORRENTS, ATTR_TORRENT_FILTER as ATTR_TORRENT_FILTER, CONF_ENTRY_ID as CONF_ENTRY_ID, DEFAULT_DELETE_DATA as DEFAULT_DELETE_DATA, DOMAIN as DOMAIN, FILTER_MODES as FILTER_MODES, SERVICE_ADD_TORRENT as SERVICE_ADD_TORRENT, SERVICE_GET_TORRENTS as SERVICE_GET_TORRENTS, SERVICE_REMOVE_TORRENT as SERVICE_REMOVE_TORRENT, SERVICE_START_TORRENT as SERVICE_START_TORRENT, SERVICE_STOP_TORRENT as SERVICE_STOP_TORRENT
from .coordinator import TransmissionDataUpdateCoordinator as TransmissionDataUpdateCoordinator
from .helpers import filter_torrents as filter_torrents, format_torrents as format_torrents
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers import selector as selector
from transmission_rpc import Torrent as Torrent
from typing import Any

_LOGGER: Incomplete

class TorrentFilter(StrEnum):
    ALL = 'all'
    STARTED = 'started'
    COMPLETED = 'completed'
    PAUSED = 'paused'
    ACTIVE = 'active'

SERVICE_BASE_SCHEMA: Incomplete
SERVICE_ADD_TORRENT_SCHEMA: Incomplete
SERVICE_GET_TORRENTS_SCHEMA: Incomplete
SERVICE_REMOVE_TORRENT_SCHEMA: Incomplete
SERVICE_START_TORRENT_SCHEMA: Incomplete
SERVICE_STOP_TORRENT_SCHEMA: Incomplete

def _get_coordinator_from_service_data(call: ServiceCall) -> TransmissionDataUpdateCoordinator: ...
async def _async_add_torrent(service: ServiceCall) -> None: ...
async def _async_get_torrents(service: ServiceCall) -> dict[str, Any] | None: ...
async def _async_start_torrent(service: ServiceCall) -> None: ...
async def _async_stop_torrent(service: ServiceCall) -> None: ...
async def _async_remove_torrent(service: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
