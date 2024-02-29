from .typing import EventType as EventType
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.const import EVENT_COMPONENT_LOADED as EVENT_COMPONENT_LOADED
from homeassistant.core import HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.loader import Integration as Integration, async_get_integrations as async_get_integrations, async_get_loaded_integration as async_get_loaded_integration, bind_hass as bind_hass
from homeassistant.setup import ATTR_COMPONENT as ATTR_COMPONENT, EventComponentLoaded as EventComponentLoaded
from homeassistant.util.logging import catch_log_exception as catch_log_exception
from types import ModuleType
from typing import Any

_LOGGER: Incomplete
DATA_INTEGRATION_PLATFORMS: str

@dataclass(slots=True, frozen=True)
class IntegrationPlatform:
    platform_name: str
    process_job: HassJob[[HomeAssistant, str, Any], Awaitable[None] | None]
    seen_components: set[str]
    def __init__(self, platform_name, process_job, seen_components) -> None: ...

def _get_platform(integration: Integration | Exception, component_name: str, platform_name: str) -> ModuleType | None: ...
def _async_process_integration_platforms_for_component(hass: HomeAssistant, integration_platforms: list[IntegrationPlatform], event: EventType[EventComponentLoaded]) -> None: ...
def _format_err(name: str, platform_name: str, *args: Any) -> str: ...
async def async_process_integration_platforms(hass: HomeAssistant, platform_name: str, process_platform: Callable[[HomeAssistant, str, Any], Awaitable[None] | None]) -> None: ...
