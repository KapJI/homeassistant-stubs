from . import DateEntity as DateEntity
from .const import DATA_COMPONENT as DATA_COMPONENT, SERVICE_SET_VALUE as SERVICE_SET_VALUE
from homeassistant.const import ATTR_DATE as ATTR_DATE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback

async def _async_set_value(entity: DateEntity, service_call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
