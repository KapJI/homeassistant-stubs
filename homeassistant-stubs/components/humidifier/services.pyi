from . import HumidifierEntity as HumidifierEntity
from .const import ATTR_HUMIDITY as ATTR_HUMIDITY, DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN, HumidifierEntityFeature as HumidifierEntityFeature, SERVICE_SET_HUMIDITY as SERVICE_SET_HUMIDITY, SERVICE_SET_MODE as SERVICE_SET_MODE
from _typeshed import Incomplete
from homeassistant.const import ATTR_MODE as ATTR_MODE, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError

_LOGGER: Incomplete

async def _async_service_humidity_set(entity: HumidifierEntity, service_call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
