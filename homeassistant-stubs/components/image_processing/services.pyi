from .const import DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN, SERVICE_SCAN as SERVICE_SCAN
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.config_validation import make_entity_service_schema as make_entity_service_schema

async def _async_scan_service(service: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
