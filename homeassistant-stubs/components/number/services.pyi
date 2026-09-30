from . import NumberEntity as NumberEntity
from .const import ATTR_VALUE as ATTR_VALUE, DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN, SERVICE_SET_VALUE as SERVICE_SET_VALUE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError

async def _async_set_value(entity: NumberEntity, service_call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
