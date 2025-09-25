from .const import DOMAIN as DOMAIN
from homeassistant.const import ATTR_COMMAND as ATTR_COMMAND
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service

ATTR_ADB_RESPONSE: str
ATTR_DEVICE_PATH: str
ATTR_HDMI_INPUT: str
ATTR_LOCAL_PATH: str
SERVICE_ADB_COMMAND: str
SERVICE_DOWNLOAD: str
SERVICE_LEARN_SENDEVENT: str
SERVICE_UPLOAD: str

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
