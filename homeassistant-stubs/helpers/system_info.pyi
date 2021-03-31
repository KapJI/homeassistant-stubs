from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.package import is_virtual_env as is_virtual_env
from typing import Any

async def async_get_system_info(hass: HomeAssistant) -> dict[str, Any]: ...
