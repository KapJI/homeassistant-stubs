from .const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID, ATTR_REQUESTED_BY as ATTR_REQUESTED_BY, ATTR_SORT_ORDER as ATTR_SORT_ORDER, ATTR_STATUS as ATTR_STATUS, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import OverseerrConfigEntry as OverseerrConfigEntry
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.util.json import JsonValueType as JsonValueType
from python_overseerr import OverseerrClient as OverseerrClient
from typing import Any

SERVICE_GET_REQUESTS: str
SERVICE_GET_REQUESTS_SCHEMA: Incomplete

def async_get_entry(hass: HomeAssistant, config_entry_id: str) -> OverseerrConfigEntry: ...
async def get_media(client: OverseerrClient, media_type: str, identifier: int) -> dict[str, Any]: ...
def setup_services(hass: HomeAssistant) -> None: ...
