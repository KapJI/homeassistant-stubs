from .const import DOMAIN as DOMAIN
from .coordinator import ImmichConfigEntry as ImmichConfigEntry
from _typeshed import Incomplete
from homeassistant.components.media_source import async_resolve_media as async_resolve_media
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.selector import MediaSelector as MediaSelector

_LOGGER: Incomplete
CONF_ALBUM_ID: str
CONF_CONFIG_ENTRY_ID: str
CONF_FILE: str
SERVICE_UPLOAD_FILE: str
SERVICE_SCHEMA_UPLOAD_FILE: Incomplete

async def _async_upload_file(service_call: ServiceCall) -> None: ...
async def async_setup_services(hass: HomeAssistant) -> None: ...
