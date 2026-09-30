from .const import DOMAIN as DOMAIN
from .coordinator import NeoPoolCoordinator as NeoPoolCoordinator
from .helpers import prepare_device_time as prepare_device_time
from _typeshed import Incomplete
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.service import async_extract_config_entry_ids as async_extract_config_entry_ids, async_register_admin_service as async_register_admin_service

_LOGGER: Incomplete
SERVICE_GET_DEVICE_TIME: str
SERVICE_SET_DEVICE_TIME: str
SERVICE_DEVICE_TIME_SCHEMA: Incomplete

async def _get_coordinator(hass: HomeAssistant, call: ServiceCall) -> NeoPoolCoordinator: ...
async def _async_get_device_time(call: ServiceCall) -> ServiceResponse: ...
async def _async_set_device_time(call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
