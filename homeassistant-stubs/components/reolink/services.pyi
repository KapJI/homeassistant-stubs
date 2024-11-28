from .const import DOMAIN as DOMAIN
from .host import ReolinkHost as ReolinkHost
from .util import get_device_uid_and_ch as get_device_uid_and_ch
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from reolink_aio.api import Chime as Chime

ATTR_RINGTONE: str

def async_setup_services(hass: HomeAssistant) -> None: ...
