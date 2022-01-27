from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import config_entry_flow as config_entry_flow

async def _async_has_devices(hass: HomeAssistant) -> bool: ...
