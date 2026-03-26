import voluptuous as vol
from .const import ATTR_DURATION as ATTR_DURATION, ATTR_PERIOD as ATTR_PERIOD, ATTR_SETPOINT as ATTR_SETPOINT, DOMAIN as DOMAIN, EvoService as EvoService
from .coordinator import EvoDataUpdateCoordinator as EvoDataUpdateCoordinator
from homeassistant.const import ATTR_MODE as ATTR_MODE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers import service as service
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.service import verify_domain_control as verify_domain_control
from typing import Any, Final

SET_ZONE_OVERRIDE_SCHEMA: Final[dict[str | vol.Marker, Any]]

def _register_zone_entity_services(hass: HomeAssistant) -> None: ...
@callback
def setup_service_functions(hass: HomeAssistant, coordinator: EvoDataUpdateCoordinator) -> None: ...
