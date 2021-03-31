from homeassistant import core as core, loader as loader, requirements as requirements
from homeassistant.config import async_notify_setup_error as async_notify_setup_error
from homeassistant.const import EVENT_COMPONENT_LOADED as EVENT_COMPONENT_LOADED, PLATFORM_FORMAT as PLATFORM_FORMAT
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.typing import ConfigType as ConfigType
from types import ModuleType
from typing import Any, Awaitable, Callable

ATTR_COMPONENT: str
BASE_PLATFORMS: Any
DATA_SETUP_DONE: str
DATA_SETUP_STARTED: str
DATA_SETUP: str
DATA_DEPS_REQS: str
SLOW_SETUP_WARNING: int
SLOW_SETUP_MAX_WAIT: int

def async_set_domains_to_be_loaded(hass: core.HomeAssistant, domains: set[str]) -> None: ...
def setup_component(hass: core.HomeAssistant, domain: str, config: ConfigType) -> bool: ...
async def async_setup_component(hass: core.HomeAssistant, domain: str, config: ConfigType) -> bool: ...
async def async_prepare_setup_platform(hass: core.HomeAssistant, hass_config: ConfigType, domain: str, platform_name: str) -> Union[ModuleType, None]: ...
async def async_process_deps_reqs(hass: core.HomeAssistant, config: ConfigType, integration: loader.Integration) -> None: ...
def async_when_setup(hass: core.HomeAssistant, component: str, when_setup_cb: Callable[[core.HomeAssistant, str], Awaitable[None]]) -> None: ...
def async_get_loaded_integrations(hass: core.HomeAssistant) -> set: ...
