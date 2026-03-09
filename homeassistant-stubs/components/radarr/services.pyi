from .const import DOMAIN as DOMAIN
from .coordinator import RadarrConfigEntry as RadarrConfigEntry
from .helpers import format_movies as format_movies, format_queue as format_queue
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import selector as selector, service as service
from typing import Any, Final

SERVICE_GET_MOVIES: Final[str]
SERVICE_GET_QUEUE: Final[str]
ATTR_MOVIES: Final[str]
ATTR_ENTRY_ID: Final[str]
CONF_MAX_ITEMS: str
DEFAULT_MAX_ITEMS: int
SERVICE_BASE_SCHEMA: Incomplete
SERVICE_GET_MOVIES_SCHEMA = SERVICE_BASE_SCHEMA
SERVICE_GET_QUEUE_SCHEMA: Incomplete

async def _handle_api_errors[_T](func: Callable[[], Awaitable[_T]]) -> _T: ...
async def _async_get_movies(call: ServiceCall) -> dict[str, Any]: ...
async def _async_get_queue(call: ServiceCall) -> dict[str, Any]: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
