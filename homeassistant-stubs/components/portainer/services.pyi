from .const import DOMAIN as DOMAIN
from .coordinator import PortainerConfigEntry as PortainerConfigEntry
from _typeshed import Incomplete
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import device_registry as dr, service as service

ATTR_DATE_UNTIL: str
ATTR_DANGLING: str
ATTR_TIMEOUT: str
ATTR_PULL_IMAGE: str
ATTR_CONTAINER_DEVICE_ID: str
SERVICE_PRUNE_IMAGES: str
SERVICE_PRUNE_IMAGES_SCHEMA: Incomplete
SERVICE_RECREATE_CONTAINER: str
SERVICE_RECREATE_CONTAINER_SCHEMA: Incomplete

@callback
def _async_get_device_and_entry(call: ServiceCall, device_id: str) -> tuple[dr.DeviceEntry, PortainerConfigEntry]: ...
@callback
def _async_get_endpoint_id(device: dr.DeviceEntry, config_entry: PortainerConfigEntry) -> int: ...
@callback
def _async_get_container_and_endpoint_ids(device: dr.DeviceEntry, config_entry: PortainerConfigEntry) -> tuple[int, str]: ...
async def prune_images(call: ServiceCall) -> None: ...
async def recreate_container(call: ServiceCall) -> None: ...
async def async_setup_services(hass: HomeAssistant) -> None: ...
