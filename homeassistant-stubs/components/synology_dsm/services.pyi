from .const import CONF_SERIAL as CONF_SERIAL, DOMAIN as DOMAIN, SERVICES as SERVICES, SERVICE_REBOOT as SERVICE_REBOOT, SERVICE_SHUTDOWN as SERVICE_SHUTDOWN
from .coordinator import SynologyDSMConfigEntry as SynologyDSMConfigEntry
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback

LOGGER: Incomplete

async def _service_handler(call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
