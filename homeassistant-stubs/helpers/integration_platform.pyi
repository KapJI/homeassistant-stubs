from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from homeassistant.const import EVENT_COMPONENT_LOADED as EVENT_COMPONENT_LOADED
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.loader import async_get_integration as async_get_integration, bind_hass as bind_hass
from homeassistant.setup import ATTR_COMPONENT as ATTR_COMPONENT
from typing import Any

_LOGGER: Incomplete
DATA_INTEGRATION_PLATFORMS: str

class IntegrationPlatform:
    platform_name: str
    process_platform: Callable[[HomeAssistant, str, Any], Awaitable[None]]
    seen_components: set[str]
    def __init__(self, platform_name, process_platform, seen_components) -> None: ...

async def _async_process_single_integration_platform_component(hass: HomeAssistant, component_name: str, integration_platform: IntegrationPlatform) -> None: ...
async def async_process_integration_platform_for_component(hass: HomeAssistant, component_name: str) -> None: ...
async def async_process_integration_platforms(hass: HomeAssistant, platform_name: str, process_platform: Callable[[HomeAssistant, str, Any], Awaitable[None]]) -> None: ...
