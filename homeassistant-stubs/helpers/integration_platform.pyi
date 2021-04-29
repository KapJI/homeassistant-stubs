from collections.abc import Awaitable
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.loader import async_get_integration as async_get_integration, bind_hass as bind_hass
from homeassistant.setup import ATTR_COMPONENT as ATTR_COMPONENT, EVENT_COMPONENT_LOADED as EVENT_COMPONENT_LOADED
from typing import Any, Callable

_LOGGER: Any

async def async_process_integration_platforms(hass: HomeAssistant, platform_name: str, process_platform: Callable[[HomeAssistant, str, Any], Awaitable[None]]) -> None: ...
