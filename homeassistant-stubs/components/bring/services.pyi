from .const import DOMAIN as DOMAIN
from .coordinator import BringConfigEntry as BringConfigEntry
from _typeshed import Incomplete
from homeassistant.components.event import ATTR_EVENT_TYPE as ATTR_EVENT_TYPE
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import service as service

ATTR_ACTIVITY: str
ATTR_ITEM_NAME: str
ATTR_NOTIFICATION_TYPE: str
ATTR_REACTION: str
ATTR_RECEIVER: str
SERVICE_PUSH_NOTIFICATION: str
SERVICE_ACTIVITY_STREAM_REACTION: str
SERVICE_ACTIVITY_STREAM_REACTION_SCHEMA: Incomplete

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
