from . import core as core, loader as loader, requirements as requirements
from .const import EVENT_COMPONENT_LOADED as EVENT_COMPONENT_LOADED, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, PLATFORM_FORMAT as PLATFORM_FORMAT, Platform as Platform
from .core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from .exceptions import DependencyError as DependencyError, HomeAssistantError as HomeAssistantError
from .helpers import translation as translation
from .helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from .helpers.typing import ConfigType as ConfigType, EventType as EventType
from .util import ensure_unique_string as ensure_unique_string
from .util.async_ import create_eager_task as create_eager_task
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Generator, Iterable
from types import ModuleType
from typing import Final, TypedDict

_LOGGER: Incomplete
ATTR_COMPONENT: Final[str]
BASE_PLATFORMS: Incomplete
DATA_SETUP: str
DATA_SETUP_DONE: str
DATA_SETUP_STARTED: str
DATA_SETUP_TIME: str
DATA_DEPS_REQS: str
DATA_PERSISTENT_ERRORS: str
NOTIFY_FOR_TRANSLATION_KEYS: Incomplete
SLOW_SETUP_WARNING: int
SLOW_SETUP_MAX_WAIT: int

class EventComponentLoaded(TypedDict):
    component: str

def async_notify_setup_error(hass: HomeAssistant, component: str, display_link: str | None = None) -> None: ...
def async_set_domains_to_be_loaded(hass: core.HomeAssistant, domains: set[str]) -> None: ...
def setup_component(hass: core.HomeAssistant, domain: str, config: ConfigType) -> bool: ...
async def async_setup_component(hass: core.HomeAssistant, domain: str, config: ConfigType) -> bool: ...
async def _async_process_dependencies(hass: core.HomeAssistant, config: ConfigType, integration: loader.Integration) -> list[str]: ...
async def _async_setup_component(hass: core.HomeAssistant, domain: str, config: ConfigType) -> bool: ...
async def async_prepare_setup_platform(hass: core.HomeAssistant, hass_config: ConfigType, domain: str, platform_name: str) -> ModuleType | None: ...
async def async_process_deps_reqs(hass: core.HomeAssistant, config: ConfigType, integration: loader.Integration) -> None: ...
def async_when_setup(hass: core.HomeAssistant, component: str, when_setup_cb: Callable[[core.HomeAssistant, str], Awaitable[None]]) -> None: ...
def async_when_setup_or_start(hass: core.HomeAssistant, component: str, when_setup_cb: Callable[[core.HomeAssistant, str], Awaitable[None]]) -> None: ...
def _async_when_setup(hass: core.HomeAssistant, component: str, when_setup_cb: Callable[[core.HomeAssistant, str], Awaitable[None]], start_event: bool) -> None: ...
def async_get_loaded_integrations(hass: core.HomeAssistant) -> set[str]: ...
def async_start_setup(hass: core.HomeAssistant, components: Iterable[str]) -> Generator[None, None, None]: ...
