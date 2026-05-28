from .const import DOMAIN as DOMAIN
from .coordinator import PortainerConfigEntry as PortainerConfigEntry
from _typeshed import Incomplete
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.service import async_extract_config_entry_ids as async_extract_config_entry_ids

ATTR_DATE_UNTIL: str
ATTR_DANGLING: str
ATTR_TIMEOUT: str
ATTR_PULL_IMAGE: str
ATTR_CONTAINER_DEVICE_ID: str
SERVICE_PRUNE_IMAGES: str
SERVICE_PRUNE_IMAGES_SCHEMA: Incomplete
SERVICE_RECREATE_CONTAINER: str
SERVICE_RECREATE_CONTAINER_SCHEMA: Incomplete

async def _extract_config_entry(service_call: ServiceCall) -> PortainerConfigEntry: ...
async def _get_endpoint_id(call: ServiceCall, config_entry: PortainerConfigEntry) -> int: ...
async def _get_container_and_endpoint_ids(call: ServiceCall) -> tuple[PortainerConfigEntry, int, str]: ...
async def prune_images(call: ServiceCall) -> None: ...
async def recreate_container(call: ServiceCall) -> None: ...
async def async_setup_services(hass: HomeAssistant) -> None: ...
