from .const import DOMAIN as DOMAIN
from .coordinator import FritzConfigEntry as FritzConfigEntry
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.service import async_extract_config_entry_ids as async_extract_config_entry_ids

_LOGGER: Incomplete
SERVICE_SET_GUEST_WIFI_PW: str
SERVICE_SCHEMA_SET_GUEST_WIFI_PW: Incomplete

async def _async_set_guest_wifi_password(service_call: ServiceCall) -> None: ...
async def async_setup_services(hass: HomeAssistant) -> None: ...
