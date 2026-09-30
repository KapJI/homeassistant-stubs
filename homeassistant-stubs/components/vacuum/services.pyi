from . import StateVacuumEntity as StateVacuumEntity
from .const import ATTR_FAN_SPEED as ATTR_FAN_SPEED, ATTR_PARAMS as ATTR_PARAMS, DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN, SERVICE_CLEAN_AREA as SERVICE_CLEAN_AREA, SERVICE_CLEAN_SPOT as SERVICE_CLEAN_SPOT, SERVICE_LOCATE as SERVICE_LOCATE, SERVICE_PAUSE as SERVICE_PAUSE, SERVICE_RETURN_TO_BASE as SERVICE_RETURN_TO_BASE, SERVICE_SEND_COMMAND as SERVICE_SEND_COMMAND, SERVICE_SET_FAN_SPEED as SERVICE_SET_FAN_SPEED, SERVICE_START as SERVICE_START, SERVICE_STOP as SERVICE_STOP, VacuumEntityFeature as VacuumEntityFeature
from _typeshed import Incomplete
from homeassistant.const import ATTR_COMMAND as ATTR_COMMAND
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError

_LOGGER: Incomplete

async def _async_clean_area(entities: list[StateVacuumEntity], call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
