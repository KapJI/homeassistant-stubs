from .const import ATTR_ATTACHMENTS as ATTR_ATTACHMENTS, ATTR_CONTENT_ID as ATTR_CONTENT_ID, ATTR_FILENAME as ATTR_FILENAME, ATTR_HTML as ATTR_HTML, ATTR_MEDIA_SOURCE as ATTR_MEDIA_SOURCE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_MESSAGE as ATTR_MESSAGE, ATTR_TITLE as ATTR_TITLE, SERVICE_SEND_MESSAGE as SERVICE_SEND_MESSAGE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service
from homeassistant.helpers.selector import MediaSelector as MediaSelector

SERVICE_SEND_MESSAGE_SCHEMA: Incomplete

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
