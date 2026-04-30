from .const import ATTR_TEXT as ATTR_TEXT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import service as service
from pyatv.interface import AppleTV as AppleTVInterface

SERVICE_SET_KEYBOARD_TEXT: str
SERVICE_SET_KEYBOARD_TEXT_SCHEMA: Incomplete
SERVICE_APPEND_KEYBOARD_TEXT: str
SERVICE_APPEND_KEYBOARD_TEXT_SCHEMA: Incomplete
SERVICE_CLEAR_KEYBOARD_TEXT: str
SERVICE_CLEAR_KEYBOARD_TEXT_SCHEMA: Incomplete

def _get_atv(call: ServiceCall) -> AppleTVInterface: ...
def _check_keyboard_focus(atv: AppleTVInterface) -> None: ...
async def _async_set_keyboard_text(call: ServiceCall) -> None: ...
async def _async_append_keyboard_text(call: ServiceCall) -> None: ...
async def _async_clear_keyboard_text(call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
