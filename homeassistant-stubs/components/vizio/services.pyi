from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service
from homeassistant.helpers.typing import VolDictType as VolDictType

SERVICE_UPDATE_SETTING: str
SERVICE_SEND_TEXT: str
ATTR_SETTING_TYPE: str
ATTR_SETTING_NAME: str
ATTR_NEW_VALUE: str
ATTR_TEXT: str
UPDATE_SETTING_SCHEMA: VolDictType
SEND_TEXT_SCHEMA: VolDictType

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
