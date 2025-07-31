from .const import DOMAIN as DOMAIN
from .coordinator import MieleConfigEntry as MieleConfigEntry
from _typeshed import Incomplete
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_TEMPERATURE as ATTR_TEMPERATURE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.service import async_extract_config_entry_ids as async_extract_config_entry_ids

ATTR_PROGRAM_ID: str
ATTR_DURATION: str
SERVICE_SET_PROGRAM: str
SERVICE_SET_PROGRAM_SCHEMA: Incomplete
SERVICE_SET_PROGRAM_OVEN: str
SERVICE_SET_PROGRAM_OVEN_SCHEMA: Incomplete
SERVICE_GET_PROGRAMS: str
SERVICE_GET_PROGRAMS_SCHEMA: Incomplete
_LOGGER: Incomplete

async def _extract_config_entry(service_call: ServiceCall) -> MieleConfigEntry: ...
async def _get_serial_number(call: ServiceCall) -> str: ...
async def set_program(call: ServiceCall) -> None: ...
async def set_program_oven(call: ServiceCall) -> None: ...
async def get_programs(call: ServiceCall) -> ServiceResponse: ...
async def async_setup_services(hass: HomeAssistant) -> None: ...
