from .const import CONF_DELETE_PERMANENTLY as CONF_DELETE_PERMANENTLY, DOMAIN as DOMAIN
from .coordinator import OneDriveConfigEntry as OneDriveConfigEntry
from _typeshed import Incomplete
from homeassistant.const import CONF_FILENAME as CONF_FILENAME
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import service as service

CONF_CONFIG_ENTRY_ID: str
CONF_DESTINATION_FOLDER: str
CONF_DESTINATION_PATH: str
UPLOAD_SERVICE: str
UPLOAD_SERVICE_SCHEMA: Incomplete
DELETE_SERVICE: str
DELETE_SERVICE_SCHEMA: Incomplete
CONTENT_SIZE_LIMIT: Incomplete

def _read_file_contents(hass: HomeAssistant, filenames: list[str]) -> list[tuple[str, bytes]]: ...
def _raise_invalid_destination_path(destination_path: str) -> None: ...
def _validate_destination_path(destination_path: str) -> str: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
