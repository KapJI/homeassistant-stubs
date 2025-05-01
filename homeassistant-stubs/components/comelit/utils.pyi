from aiohttp import ClientSession as ClientSession
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client

async def async_client_session(hass: HomeAssistant) -> ClientSession: ...
