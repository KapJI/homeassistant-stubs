from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.core import async_get_hass_or_none as async_get_hass_or_none
from homeassistant.helpers.frame import MissingIntegrationFrame as MissingIntegrationFrame, get_current_frame as get_current_frame, get_integration_frame as get_integration_frame
from homeassistant.loader import async_suggest_report_issue as async_suggest_report_issue
from typing import Any

_LOGGER: Incomplete

def _get_line_from_cache(filename: str, lineno: int) -> str: ...
def raise_for_blocking_call(func: Callable[..., Any], check_allowed: Callable[[dict[str, Any]], bool] | None = None, strict: bool = True, strict_core: bool = True, advise_msg: str | None = None, **mapped_args: Any) -> None: ...
def protect_loop(func: Callable[_P, _R], loop_thread_id: int, strict: bool = True, strict_core: bool = True, check_allowed: Callable[[dict[str, Any]], bool] | None = None) -> Callable[_P, _R]: ...
