from .camera import CAMERA_SERVICES as CAMERA_SERVICES
from .const import CAMERAS as CAMERAS, DATA_AMCREST as DATA_AMCREST, DOMAIN as DOMAIN
from .helpers import service_signal as service_signal
from homeassistant.auth.models import User as User
from homeassistant.auth.permissions.const import POLICY_CONTROL as POLICY_CONTROL
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ENTITY_MATCH_ALL as ENTITY_MATCH_ALL, ENTITY_MATCH_NONE as ENTITY_MATCH_NONE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import Unauthorized as Unauthorized, UnknownUser as UnknownUser
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.service import async_extract_entity_ids as async_extract_entity_ids

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
