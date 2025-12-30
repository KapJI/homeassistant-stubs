from .const import BCU_APP as BCU_APP, CHARGING_CARD_ID as CHARGING_CARD_ID, DOMAIN as DOMAIN, SERVICE_START_CHARGE_SESSION as SERVICE_START_CHARGE_SESSION
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError

SERVICE_START_CHARGE_SESSION_SCHEMA: Incomplete

async def start_charge_session(service_call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
