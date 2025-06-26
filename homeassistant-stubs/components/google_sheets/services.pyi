from . import GoogleSheetsConfigEntry as GoogleSheetsConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.selector import ConfigEntrySelector as ConfigEntrySelector

DATA: str
DATA_CONFIG_ENTRY: str
WORKSHEET: str
SERVICE_APPEND_SHEET: str
SHEET_SERVICE_SCHEMA: Incomplete

def _append_to_sheet(call: ServiceCall, entry: GoogleSheetsConfigEntry) -> None: ...
async def _async_append_to_sheet(call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
