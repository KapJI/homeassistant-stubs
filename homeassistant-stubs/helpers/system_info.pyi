from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.package import is_docker_env as is_docker_env, is_virtual_env as is_virtual_env
from typing import Any

_LOGGER: Incomplete

def is_official_image() -> bool: ...

cached_get_user: Incomplete

async def async_get_system_info(hass: HomeAssistant) -> dict[str, Any]: ...
