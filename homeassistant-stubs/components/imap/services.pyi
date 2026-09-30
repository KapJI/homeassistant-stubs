from .const import DOMAIN as DOMAIN
from .coordinator import ImapMessage as ImapMessage, connect_to_server as connect_to_server, get_parts as get_parts
from .errors import InvalidAuth as InvalidAuth, InvalidFolder as InvalidFolder
from _typeshed import Incomplete
from aioimaplib import IMAP4_SSL as IMAP4_SSL, Response as Response
from email.message import Message
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError

_LOGGER: Incomplete
CONF_ENTRY: str
CONF_SEEN: str
CONF_PART: str
CONF_UID: str
CONF_TARGET_FOLDER: str
_SERVICE_UID_SCHEMA: Incomplete
SERVICE_SEEN_SCHEMA = _SERVICE_UID_SCHEMA
SERVICE_MOVE_SCHEMA: Incomplete
SERVICE_DELETE_SCHEMA = _SERVICE_UID_SCHEMA
SERVICE_FETCH_TEXT_SCHEMA = _SERVICE_UID_SCHEMA
SERVICE_FETCH_PART_SCHEMA: Incomplete

async def async_get_imap_client(hass: HomeAssistant, entry_id: str) -> IMAP4_SSL: ...
@callback
def raise_on_error(response: Response, translation_key: str) -> None: ...
@callback
def _get_message_part(message: Message, part_key: str) -> Message: ...
async def _async_seen(call: ServiceCall) -> None: ...
async def _async_move(call: ServiceCall) -> None: ...
async def _async_delete(call: ServiceCall) -> None: ...
async def _async_fetch(call: ServiceCall) -> ServiceResponse: ...
async def _async_fetch_part(call: ServiceCall) -> ServiceResponse: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
