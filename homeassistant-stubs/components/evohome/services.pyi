import voluptuous as vol
from .const import ATTR_DURATION as ATTR_DURATION, ATTR_PERIOD as ATTR_PERIOD, ATTR_SETPOINT as ATTR_SETPOINT, DOMAIN as DOMAIN, EvoService as EvoService, RESET_BREAKS_IN_HA_VERSION as RESET_BREAKS_IN_HA_VERSION, SERVICE_BREAKS_IN_HA_VERSION as SERVICE_BREAKS_IN_HA_VERSION
from .coordinator import EvoDataUpdateCoordinator as EvoDataUpdateCoordinator
from .helpers import async_create_deprecation_issue_once as async_create_deprecation_issue_once
from evohomeasync2 import ControlSystem as ControlSystem
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_MODE as ATTR_MODE, ATTR_STATE as ATTR_STATE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers import service as service
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.service import verify_domain_control as verify_domain_control
from typing import Any, Final

SET_SYSTEM_MODE_SCHEMA: Final[dict[str | vol.Marker, Any]]
SET_ZONE_OVERRIDE_SCHEMA: Final[dict[str | vol.Marker, Any]]
SET_DHW_OVERRIDE_SCHEMA: Final[dict[str | vol.Marker, Any]]

def _register_zone_entity_services(hass: HomeAssistant) -> None: ...
def _resolve_ctl_unique_id(hass: HomeAssistant, call: ServiceCall, tcs_id: str) -> str: ...
def _register_dhw_entity_services(hass: HomeAssistant) -> None: ...
def _validate_set_system_mode_params(tcs: ControlSystem, data: dict[str, Any]) -> None: ...
@callback
def setup_service_functions(hass: HomeAssistant, coordinator: EvoDataUpdateCoordinator) -> None: ...
