from homeassistant.components.network import async_get_source_ip as async_get_source_ip
from homeassistant.core import HomeAssistant as HomeAssistant

async def async_get_event_callback_host(hass: HomeAssistant, upnp_location: str) -> str: ...
