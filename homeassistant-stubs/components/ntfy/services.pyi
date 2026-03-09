from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_MESSAGE as ATTR_MESSAGE, ATTR_TITLE as ATTR_TITLE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service
from homeassistant.helpers.selector import MediaSelector as MediaSelector
from typing import Any

SERVICE_PUBLISH: str
SERVICE_CLEAR: str
SERVICE_DELETE: str
ATTR_ATTACH: str
ATTR_CALL: str
ATTR_CLICK: str
ATTR_DELAY: str
ATTR_EMAIL: str
ATTR_ICON: str
ATTR_MARKDOWN: str
ATTR_PRIORITY: str
ATTR_TAGS: str
ATTR_SEQUENCE_ID: str
ATTR_ATTACH_FILE: str
ATTR_FILENAME: str
GRP_ATTACHMENT: str
MSG_ATTACHMENT: str
ATTR_ACTIONS: str
ATTR_ACTION: str
ATTR_VIEW: str
ATTR_BROADCAST: str
ATTR_HTTP: str
ATTR_LABEL: str
ATTR_URL: str
ATTR_CLEAR: str
ATTR_INTENT: str
ATTR_EXTRAS: str
ATTR_METHOD: str
ATTR_HEADERS: str
ATTR_BODY: str
ATTR_VALUE: str
ATTR_COPY: str
ACTIONS_MAP: Incomplete
MAX_ACTIONS_ALLOWED: int

def validate_filename(params: dict[str, Any]) -> dict[str, Any]: ...

ACTION_SCHEMA: Incomplete
VIEW_SCHEMA: Incomplete
BROADCAST_SCHEMA: Incomplete
HTTP_SCHEMA: Incomplete
COPY_SCHEMA: Incomplete
SERVICE_PUBLISH_SCHEMA: Incomplete
SERVICE_CLEAR_DELETE_SCHEMA: Incomplete

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
