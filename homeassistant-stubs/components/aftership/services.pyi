from . import AfterShipConfigEntry as AfterShipConfigEntry
from .const import ADD_TRACKING_SERVICE_SCHEMA as ADD_TRACKING_SERVICE_SCHEMA, CONF_SLUG as CONF_SLUG, CONF_TITLE as CONF_TITLE, CONF_TRACKING_NUMBER as CONF_TRACKING_NUMBER, DOMAIN as DOMAIN, REMOVE_TRACKING_SERVICE_SCHEMA as REMOVE_TRACKING_SERVICE_SCHEMA, SERVICE_ADD_TRACKING as SERVICE_ADD_TRACKING, SERVICE_REMOVE_TRACKING as SERVICE_REMOVE_TRACKING, UPDATE_TOPIC as UPDATE_TOPIC
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers import service as service
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send

async def handle_add_tracking(call: ServiceCall) -> None: ...
async def handle_remove_tracking(call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
