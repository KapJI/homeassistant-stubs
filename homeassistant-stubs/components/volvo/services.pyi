from .const import DOMAIN as DOMAIN
from .coordinator import VolvoConfigEntry as VolvoConfigEntry
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, SupportsResponse as SupportsResponse
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from httpx import AsyncClient as AsyncClient
from typing import Any

_LOGGER: Incomplete
CONF_CONFIG_ENTRY_ID: str
CONF_IMAGE_TYPES: str
SERVICE_GET_IMAGE_URL: str
SERVICE_GET_IMAGE_URL_SCHEMA: Incomplete
_HEADERS: Incomplete
_PARAM_IMAGE_ANGLE_MAP: Incomplete
_IMAGE_ANGLE_MAP: Incomplete

async def async_setup_services(hass: HomeAssistant) -> None: ...
async def _get_image_url(call: ServiceCall) -> dict[str, Any]: ...
def _async_get_config_entry(hass: HomeAssistant, entry_id: str) -> VolvoConfigEntry: ...
def _get_requested_image_types(requested_image_types: list[str]) -> list[str]: ...
def _parse_exterior_image_url(exterior_url: str, angle: str) -> str: ...
async def _async_image_exists(client: AsyncClient, url: str) -> bool: ...
