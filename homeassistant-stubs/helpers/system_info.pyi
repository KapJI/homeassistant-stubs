from .typing import HomeAssistantType as HomeAssistantType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.package import is_virtual_env as is_virtual_env
from typing import Any, Dict

async def async_get_system_info(hass: HomeAssistantType) -> Dict[str, Any]: ...
