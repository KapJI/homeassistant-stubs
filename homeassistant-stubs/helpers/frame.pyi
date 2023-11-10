from _typeshed import Incomplete
from collections.abc import Callable
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant, async_get_hass as async_get_hass
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.loader import async_suggest_report_issue as async_suggest_report_issue
from traceback import FrameSummary
from typing import TypeVar

_LOGGER: Incomplete
_REPORTED_INTEGRATIONS: set[str]
_CallableT = TypeVar('_CallableT', bound=Callable)

@dataclass(kw_only=True)
class IntegrationFrame:
    custom_integration: bool
    frame: FrameSummary
    integration: str
    module: str | None
    relative_filename: str
    def __init__(self, *, custom_integration, frame, integration, module, relative_filename) -> None: ...

def get_integration_frame(exclude_integrations: set | None = ...) -> IntegrationFrame: ...

class MissingIntegrationFrame(HomeAssistantError): ...

def report(what: str, exclude_integrations: set | None = ..., error_if_core: bool = ..., level: int = ...) -> None: ...
def _report_integration(what: str, integration_frame: IntegrationFrame, level: int = ...) -> None: ...
def warn_use(func: _CallableT, what: str) -> _CallableT: ...
