from . import TimeEntity as TimeEntity
from .const import DATA_COMPONENT as DATA_COMPONENT, SERVICE_SET_VALUE as SERVICE_SET_VALUE
from homeassistant.const import ATTR_TIME as ATTR_TIME
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback

async def _async_set_value(entity: TimeEntity, service_call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
