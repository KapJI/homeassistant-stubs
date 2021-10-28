from collections.abc import Mapping
from homeassistant.components import websocket_api as websocket_api
from homeassistant.const import ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.helpers.entity import async_generate_entity_id as async_generate_entity_id
from homeassistant.helpers.template import Template as Template, is_template_string as is_template_string
from homeassistant.helpers.typing import ConfigType as ConfigType
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
SCHEMA_SERVICE_NOTIFICATION: Any
DEFAULT_OBJECT_ID: str
_LOGGER: Any
STATE: str
STATUS_UNREAD: str
STATUS_READ: str

def create(hass: HomeAssistant, message: str, title: Union[str, None] = ..., notification_id: Union[str, None] = ...) -> None: ...
def dismiss(hass: HomeAssistant, notification_id: str) -> None: ...
def async_create(hass: HomeAssistant, message: str, title: Union[str, None] = ..., notification_id: Union[str, None] = ..., *, context: Union[Context, None] = ...) -> None: ...
def async_dismiss(hass: HomeAssistant, notification_id: str, *, context: Union[Context, None] = ...) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def websocket_get_notifications(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: Mapping[str, Any]) -> None: ...
