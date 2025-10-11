from .const import DOMAIN as DOMAIN, _LOGGER as _LOGGER
from .coordinator import AmazonDevicesCoordinator as AmazonDevicesCoordinator
from .entity import AmazonEntity as AmazonEntity
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate

def alexa_api_call[_T: AmazonEntity, **_P](func: Callable[Concatenate[_T, _P], Awaitable[None]]) -> Callable[Concatenate[_T, _P], Coroutine[Any, Any, None]]: ...
async def async_update_unique_id(hass: HomeAssistant, coordinator: AmazonDevicesCoordinator, domain: str, old_key: str, new_key: str) -> None: ...
async def async_remove_dnd_from_virtual_group(hass: HomeAssistant, coordinator: AmazonDevicesCoordinator) -> None: ...
