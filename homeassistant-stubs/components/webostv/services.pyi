from .const import ATTR_PAYLOAD as ATTR_PAYLOAD, ATTR_SOUND_OUTPUT as ATTR_SOUND_OUTPUT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import ATTR_COMMAND as ATTR_COMMAND
from homeassistant.core import HomeAssistant as HomeAssistant, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.helpers import service as service
from homeassistant.helpers.typing import VolDictType as VolDictType

ATTR_BUTTON: str
SERVICE_BUTTON: str
SERVICE_COMMAND: str
SERVICE_SELECT_SOUND_OUTPUT: str
BUTTON_SCHEMA: VolDictType
COMMAND_SCHEMA: VolDictType
SOUND_OUTPUT_SCHEMA: VolDictType
SERVICES: Incomplete

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
