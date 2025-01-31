from .const import ATTR_PASSWORD as ATTR_PASSWORD, ATTR_USERNAME as ATTR_USERNAME, DOMAIN as DOMAIN, SERVICE_SIGN_IN as SERVICE_SIGN_IN, SERVICE_SIGN_OUT as SERVICE_SIGN_OUT
from .coordinator import HeosConfigEntry as HeosConfigEntry
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from pyheos import Heos as Heos

_LOGGER: Incomplete
HEOS_SIGN_IN_SCHEMA: Incomplete
HEOS_SIGN_OUT_SCHEMA: Incomplete

def register(hass: HomeAssistant) -> None: ...
def _get_controller(hass: HomeAssistant) -> Heos: ...
async def _sign_in_handler(service: ServiceCall) -> None: ...
async def _sign_out_handler(service: ServiceCall) -> None: ...
