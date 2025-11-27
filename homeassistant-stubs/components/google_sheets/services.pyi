from . import GoogleSheetsConfigEntry as GoogleSheetsConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.selector import ConfigEntrySelector as ConfigEntrySelector
from homeassistant.util.json import JsonObjectType as JsonObjectType

ADD_CREATED_COLUMN: str
DATA: str
DATA_CONFIG_ENTRY: str
ROWS: str
WORKSHEET: str
SERVICE_APPEND_SHEET: str
SERVICE_GET_SHEET: str
SHEET_SERVICE_SCHEMA: Incomplete
get_SHEET_SERVICE_SCHEMA: Incomplete

def _append_to_sheet(call: ServiceCall, entry: GoogleSheetsConfigEntry) -> None: ...
def _get_from_sheet(call: ServiceCall, entry: GoogleSheetsConfigEntry) -> JsonObjectType: ...
async def _async_append_to_sheet(call: ServiceCall) -> None: ...
async def _async_get_from_sheet(call: ServiceCall) -> ServiceResponse: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
