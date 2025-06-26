from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.dispatcher import dispatcher_send as dispatcher_send

SERVICE_SETTINGS: str
SERVICE_CAPTURE_IMAGE: str
SERVICE_TRIGGER_AUTOMATION: str
ATTR_SETTING: str
ATTR_VALUE: str
CHANGE_SETTING_SCHEMA: Incomplete
CAPTURE_IMAGE_SCHEMA: Incomplete
AUTOMATION_SCHEMA: Incomplete

def _change_setting(call: ServiceCall) -> None: ...
def _capture_image(call: ServiceCall) -> None: ...
def _trigger_automation(call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
