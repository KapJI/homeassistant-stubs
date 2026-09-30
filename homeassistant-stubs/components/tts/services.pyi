from .const import ATTR_CACHE as ATTR_CACHE, ATTR_LANGUAGE as ATTR_LANGUAGE, ATTR_MEDIA_PLAYER_ENTITY_ID as ATTR_MEDIA_PLAYER_ENTITY_ID, ATTR_MESSAGE as ATTR_MESSAGE, ATTR_OPTIONS as ATTR_OPTIONS, DATA_COMPONENT as DATA_COMPONENT, DATA_TTS_MANAGER as DATA_TTS_MANAGER, DEFAULT_CACHE as DEFAULT_CACHE, DOMAIN as DOMAIN, SERVICE_CLEAR_CACHE as SERVICE_CLEAR_CACHE
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback

SCHEMA_SERVICE_CLEAR_CACHE: Incomplete

async def _async_clear_cache_handle(service: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
