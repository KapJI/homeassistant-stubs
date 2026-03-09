from .const import ATTR_DURATION as ATTR_DURATION, ATTR_DURATION_UNTIL as ATTR_DURATION_UNTIL, ATTR_PERIOD as ATTR_PERIOD, ATTR_SETPOINT as ATTR_SETPOINT, DOMAIN as DOMAIN, EvoService as EvoService
from .coordinator import EvoDataUpdateCoordinator as EvoDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_MODE as ATTR_MODE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.service import verify_domain_control as verify_domain_control
from typing import Final

RESET_ZONE_OVERRIDE_SCHEMA: Final[Incomplete]
SET_ZONE_OVERRIDE_SCHEMA: Final[Incomplete]

@callback
def setup_service_functions(hass: HomeAssistant, coordinator: EvoDataUpdateCoordinator) -> None: ...
