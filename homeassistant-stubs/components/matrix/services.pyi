from . import MatrixBot as MatrixBot
from .const import ATTR_FORMAT as ATTR_FORMAT, ATTR_IMAGES as ATTR_IMAGES, ATTR_MESSAGE_ID as ATTR_MESSAGE_ID, ATTR_REACTION as ATTR_REACTION, ATTR_ROOM as ATTR_ROOM, ATTR_THREAD_ID as ATTR_THREAD_ID, CONF_ROOMS_REGEX as CONF_ROOMS_REGEX, DOMAIN as DOMAIN, FORMAT_HTML as FORMAT_HTML, FORMAT_TEXT as FORMAT_TEXT, SERVICE_REACT as SERVICE_REACT, SERVICE_SEND_MESSAGE as SERVICE_SEND_MESSAGE
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_MESSAGE as ATTR_MESSAGE, ATTR_TARGET as ATTR_TARGET
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback

MESSAGE_FORMATS: Incomplete
DEFAULT_MESSAGE_FORMAT = FORMAT_TEXT
SERVICE_SCHEMA_SEND_MESSAGE: Incomplete
SERVICE_SCHEMA_REACT: Incomplete

async def _handle_send_message(call: ServiceCall) -> None: ...
async def _handle_react(call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
