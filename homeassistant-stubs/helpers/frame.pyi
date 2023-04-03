from _typeshed import Incomplete
from collections.abc import Callable
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from traceback import FrameSummary
from typing import TypeVar

_LOGGER: Incomplete
_REPORTED_INTEGRATIONS: set[str]
_CallableT = TypeVar('_CallableT', bound=Callable)

def get_integration_frame(exclude_integrations: set | None = ...) -> tuple[FrameSummary, str, str]: ...

class MissingIntegrationFrame(HomeAssistantError): ...

def report(what: str, exclude_integrations: set | None = ..., error_if_core: bool = ..., level: int = ...) -> None: ...
def report_integration(what: str, integration_frame: tuple[FrameSummary, str, str], level: int = ...) -> None: ...
def warn_use(func: _CallableT, what: str) -> _CallableT: ...
