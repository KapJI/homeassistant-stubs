from .const import ATTR_EVENT as ATTR_EVENT, DATA_RFXOBJECT as DATA_RFXOBJECT, DOMAIN as DOMAIN, SERVICE_SEND as SERVICE_SEND
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

def _bytearray_string(data: Any) -> bytearray: ...

SERVICE_SEND_SCHEMA: Incomplete

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
