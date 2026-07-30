from .const import ATTR_MEDIA_ID as ATTR_MEDIA_ID, ATTR_MEDIA_TYPE as ATTR_MEDIA_TYPE, ATTR_QUERY as ATTR_QUERY, ATTR_REQUESTED_BY as ATTR_REQUESTED_BY, ATTR_SEASONS as ATTR_SEASONS, ATTR_SORT_ORDER as ATTR_SORT_ORDER, ATTR_STATUS as ATTR_STATUS, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import OverseerrConfigEntry as OverseerrConfigEntry
from _typeshed import Incomplete
from homeassistant.const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import service as service
from homeassistant.util.json import JsonValueType as JsonValueType
from python_overseerr import OverseerrClient as OverseerrClient
from typing import Any, Literal

SERVICE_GET_REQUESTS: str
SERVICE_SEARCH_MEDIA: str
SERVICE_REQUEST_MEDIA: str
SERVICE_GET_REQUESTS_SCHEMA: Incomplete
SERVICE_SEARCH_MEDIA_SCHEMA: Incomplete
SERVICE_REQUEST_MEDIA_SCHEMA: Incomplete

async def _get_media(client: OverseerrClient, media_type: str, identifier: int) -> dict[str, Any]: ...
async def _async_get_requests(call: ServiceCall) -> ServiceResponse: ...
async def _async_search_media(call: ServiceCall) -> ServiceResponse: ...
async def _async_request_media(call: ServiceCall) -> ServiceResponse: ...
def parse_seasons_input(seasons_input: Any | None) -> Literal['all'] | list[int]: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
