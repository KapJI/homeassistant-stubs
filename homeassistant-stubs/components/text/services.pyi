from . import TextEntity as TextEntity
from .const import ATTR_VALUE as ATTR_VALUE, DATA_COMPONENT as DATA_COMPONENT, SERVICE_SET_VALUE as SERVICE_SET_VALUE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback

async def _async_set_value(entity: TextEntity, service_call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
