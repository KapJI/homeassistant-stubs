from . import MatrixBot as MatrixBot
from .const import ATTR_FORMAT as ATTR_FORMAT, ATTR_IMAGES as ATTR_IMAGES, CONF_ROOMS_REGEX as CONF_ROOMS_REGEX, DOMAIN as DOMAIN, FORMAT_HTML as FORMAT_HTML, FORMAT_TEXT as FORMAT_TEXT, SERVICE_SEND_MESSAGE as SERVICE_SEND_MESSAGE
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_MESSAGE as ATTR_MESSAGE, ATTR_TARGET as ATTR_TARGET
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall

MESSAGE_FORMATS: Incomplete
DEFAULT_MESSAGE_FORMAT = FORMAT_TEXT
SERVICE_SCHEMA_SEND_MESSAGE: Incomplete

async def _handle_send_message(call: ServiceCall) -> None: ...
def register_services(hass: HomeAssistant) -> None: ...
