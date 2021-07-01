from collections.abc import Mapping
from homeassistant.components import websocket_api as websocket_api
from homeassistant.const import ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.helpers.entity import async_generate_entity_id as async_generate_entity_id
from homeassistant.helpers.template import Template as Template
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util import slugify as slugify
from typing import Any

ATTR_CREATED_AT: str
ATTR_MESSAGE: str
ATTR_NOTIFICATION_ID: str
ATTR_TITLE: str
ATTR_STATUS: str
DOMAIN: str
ENTITY_ID_FORMAT: Any
EVENT_PERSISTENT_NOTIFICATIONS_UPDATED: str
SERVICE_CREATE: str
SERVICE_DISMISS: str
SERVICE_MARK_READ: str
SCHEMA_SERVICE_CREATE: Any
SCHEMA_SERVICE_DISMISS: Any
SCHEMA_SERVICE_MARK_READ: Any
DEFAULT_OBJECT_ID: str
_LOGGER: Any
STATE: str
STATUS_UNREAD: str
STATUS_READ: str

def create(hass, message, title: Any | None = ..., notification_id: Any | None = ...) -> None: ...
def dismiss(hass, notification_id) -> None: ...
def async_create(hass: HomeAssistant, message: str, title: Union[str, None] = ..., notification_id: Union[str, None] = ...) -> None: ...
def async_dismiss(hass: HomeAssistant, notification_id: str) -> None: ...
async def async_setup(hass: HomeAssistant, config: dict) -> bool: ...
def websocket_get_notifications(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: Mapping[str, Any]) -> None: ...
