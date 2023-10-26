from .frame import MissingIntegrationFrame as MissingIntegrationFrame, get_integration_frame as get_integration_frame
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.core import HomeAssistant as HomeAssistant, async_get_hass as async_get_hass
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.loader import async_suggest_report_issue as async_suggest_report_issue
from typing import Any, TypeVar

_ObjectT = TypeVar('_ObjectT', bound=object)
_R = TypeVar('_R')
_P: Incomplete

def deprecated_substitute(substitute_name: str) -> Callable[[Callable[[_ObjectT], Any]], Callable[[_ObjectT], Any]]: ...
def get_deprecated(config: dict[str, Any], new_name: str, old_name: str, default: Any | None = ...) -> Any | None: ...
def deprecated_class(replacement: str) -> Callable[[Callable[_P, _R]], Callable[_P, _R]]: ...
def deprecated_function(replacement: str) -> Callable[[Callable[_P, _R]], Callable[_P, _R]]: ...
def _print_deprecation_warning(obj: Any, replacement: str, description: str) -> None: ...
