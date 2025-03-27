from .const import DATA_SESSION as DATA_SESSION, DOMAIN as DOMAIN
from aiohttp import ClientSession as ClientSession
from homeassistant.const import EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback

async def async_get_client_session(hass: HomeAssistant) -> ClientSession: ...
