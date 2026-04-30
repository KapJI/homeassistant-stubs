from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.const import SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, TemplateError as TemplateError
from homeassistant.helpers import template as template
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.json import JsonObjectType as JsonObjectType
from typing import Any

DOMAIN: str
COMMAND_TIMEOUT: int
_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

def _make_handler(cmd: str, hass: HomeAssistant, cache: dict[str, tuple[str, str | None, template.Template | None]]) -> Callable[[ServiceCall], Coroutine[Any, Any, ServiceResponse]]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
