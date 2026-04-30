from .const import ATTR_INTERVAL as ATTR_INTERVAL, ATTR_RULE as ATTR_RULE, DOMAIN as DOMAIN, MAX_LOCK_RULE_INTERVAL as MAX_LOCK_RULE_INTERVAL, MIN_LOCK_RULE_INTERVAL as MIN_LOCK_RULE_INTERVAL, SERVICE_SET_LOCK_RULE as SERVICE_SET_LOCK_RULE
from .coordinator import UnifiAccessConfigEntry as UnifiAccessConfigEntry
from _typeshed import Incomplete
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import service as service

LOCK_RULE_OPTIONS: Incomplete
SERVICE_SET_LOCK_RULE_SCHEMA: Incomplete

@callback
def _async_get_target(hass: HomeAssistant, call: ServiceCall) -> tuple[UnifiAccessConfigEntry, str]: ...
async def async_setup_services(hass: HomeAssistant) -> None: ...
