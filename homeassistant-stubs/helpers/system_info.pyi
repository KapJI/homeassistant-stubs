from .importlib import async_import_module as async_import_module
from .singleton import singleton as singleton
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.package import is_docker_env as is_docker_env, is_virtual_env as is_virtual_env
from typing import Any

_LOGGER: Incomplete
_DATA_MAC_VER: str

def is_official_image() -> bool: ...
async def async_get_mac_ver(hass: HomeAssistant) -> str: ...

cached_get_user: Incomplete

async def async_get_system_info(hass: HomeAssistant) -> dict[str, Any]: ...
