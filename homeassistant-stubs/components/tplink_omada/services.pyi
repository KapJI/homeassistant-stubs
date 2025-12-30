from .const import DOMAIN as DOMAIN
from .controller import OmadaSiteController as OmadaSiteController
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import selector as selector

SERVICE_RECONNECT_CLIENT: str
ATTR_CONFIG_ENTRY_ID: str
ATTR_MAC: str

def _get_controller(call: ServiceCall) -> OmadaSiteController: ...

SCHEMA_RECONNECT_CLIENT: Incomplete

async def _handle_reconnect_client(call: ServiceCall) -> None: ...

SERVICES: Incomplete

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
