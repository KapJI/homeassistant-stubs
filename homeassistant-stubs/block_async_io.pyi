from .helpers.frame import get_current_frame as get_current_frame
from .util.loop import protect_loop as protect_loop
from _typeshed import Incomplete
from typing import Any

_IN_TESTS: Incomplete

def _check_import_call_allowed(mapped_args: dict[str, Any]) -> bool: ...
def _check_sleep_call_allowed(mapped_args: dict[str, Any]) -> bool: ...
def enable() -> None: ...
