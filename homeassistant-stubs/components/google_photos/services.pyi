from .const import DOMAIN as DOMAIN, UPLOAD_SCOPE as UPLOAD_SCOPE
from .coordinator import GooglePhotosConfigEntry as GooglePhotosConfigEntry
from _typeshed import Incomplete
from homeassistant.const import CONF_FILENAME as CONF_FILENAME
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError

CONF_CONFIG_ENTRY_ID: str
CONF_ALBUM: str
UPLOAD_SERVICE: str
UPLOAD_SERVICE_SCHEMA: Incomplete
CONTENT_SIZE_LIMIT: Incomplete

def _read_file_contents(hass: HomeAssistant, filenames: list[str]) -> list[tuple[str, bytes]]: ...
async def _async_handle_upload(call: ServiceCall) -> ServiceResponse: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
