from .const import DATA_COMPONENT as DATA_COMPONENT, LockEntityFeature as LockEntityFeature
from _typeshed import Incomplete
from homeassistant.const import ATTR_CODE as ATTR_CODE, SERVICE_LOCK as SERVICE_LOCK, SERVICE_OPEN as SERVICE_OPEN, SERVICE_UNLOCK as SERVICE_UNLOCK
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

LOCK_SERVICE_SCHEMA: Incomplete

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
