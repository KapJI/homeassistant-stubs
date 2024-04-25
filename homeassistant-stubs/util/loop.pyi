from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.core import HomeAssistant as HomeAssistant, async_get_hass as async_get_hass
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.frame import MissingIntegrationFrame as MissingIntegrationFrame, get_current_frame as get_current_frame, get_integration_frame as get_integration_frame
from homeassistant.loader import async_suggest_report_issue as async_suggest_report_issue
from typing import Any, ParamSpec, TypeVar

_LOGGER: Incomplete
_R = TypeVar('_R')
_P = ParamSpec('_P')

def _get_line_from_cache(filename: str, lineno: int) -> str: ...
def check_loop(func: Callable[..., Any], check_allowed: Callable[[dict[str, Any]], bool] | None = None, strict: bool = True, strict_core: bool = True, advise_msg: str | None = None, **mapped_args: Any) -> None: ...
def protect_loop(func: Callable[_P, _R], strict: bool = True, strict_core: bool = True, check_allowed: Callable[[dict[str, Any]], bool] | None = None) -> Callable[_P, _R]: ...
