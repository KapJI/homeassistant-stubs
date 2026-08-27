from .const import AFFECTS_TO_ACTIVE_PROGRAM as AFFECTS_TO_ACTIVE_PROGRAM, AFFECTS_TO_SELECTED_PROGRAM as AFFECTS_TO_SELECTED_PROGRAM, ATTR_AFFECTS_TO as ATTR_AFFECTS_TO, ATTR_KEY as ATTR_KEY, ATTR_PROGRAM as ATTR_PROGRAM, ATTR_VALUE as ATTR_VALUE, DOMAIN as DOMAIN, PROGRAM_ENUM_OPTIONS as PROGRAM_ENUM_OPTIONS, SERVICE_SETTING as SERVICE_SETTING, SERVICE_SET_PROGRAM_AND_OPTIONS as SERVICE_SET_PROGRAM_AND_OPTIONS, SERVICE_START_SELECTED_PROGRAM as SERVICE_START_SELECTED_PROGRAM, TRANSLATION_KEYS_PROGRAMS_MAP as TRANSLATION_KEYS_PROGRAMS_MAP
from .coordinator import HomeConnectConfigEntry as HomeConnectConfigEntry
from .utils import bsh_key_to_translation_key as bsh_key_to_translation_key, get_dict_from_home_connect_error as get_dict_from_home_connect_error
from _typeshed import Incomplete
from aiohomeconnect.client import Client as HomeConnectClient
from aiohomeconnect.model import Option
from aiohomeconnect.model.program import Program as Program, ProgramDefinition as ProgramDefinition
from collections.abc import Awaitable, Callable as Callable
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import service as service
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter

LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
PROGRAM_OPTIONS: Incomplete
SERVICE_SETTING_SCHEMA: Incomplete
TEMPERATURE_OPTIONS: Incomplete

def _require_program_or_at_least_one_option(data: dict) -> dict: ...

SERVICE_PROGRAM_AND_OPTIONS_SCHEMA: Incomplete
SERVICE_START_SELECTED_PROGRAM_SCHEMA: Incomplete

async def _get_client_and_ha_id(hass: HomeAssistant, device_id: str) -> tuple[HomeConnectClient, str]: ...
async def async_service_setting(call: ServiceCall) -> None: ...
async def _check_temperature_options(options: list[Option], method_call: Callable[..., Awaitable[Program | ProgramDefinition]]) -> None: ...
async def async_service_set_program_and_options(call: ServiceCall) -> None: ...
async def async_service_start_selected_program(call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
