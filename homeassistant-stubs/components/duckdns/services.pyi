from .const import ATTR_CONFIG_ENTRY as ATTR_CONFIG_ENTRY, ATTR_TXT as ATTR_TXT, DOMAIN as DOMAIN, SERVICE_SET_TXT as SERVICE_SET_TXT
from .helpers import update_duckdns as update_duckdns
from _typeshed import Incomplete
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_DOMAIN as CONF_DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import service as service
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import ConfigEntrySelector as ConfigEntrySelector

SERVICE_TXT_SCHEMA: Incomplete

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
async def update_domain_service(call: ServiceCall) -> None: ...
