import logging
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from functools import cached_property as cached_property
from homeassistant.core import async_get_hass_or_none as async_get_hass_or_none
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.loader import async_suggest_report_issue as async_suggest_report_issue
from types import FrameType

_LOGGER: Incomplete
_REPORTED_INTEGRATIONS: set[str]

@dataclass(kw_only=True)
class IntegrationFrame:
    custom_integration: bool
    integration: str
    module: str | None
    relative_filename: str
    frame: FrameType
    @cached_property
    def line_number(self) -> int: ...
    @cached_property
    def filename(self) -> str: ...
    @cached_property
    def line(self) -> str: ...
    def __init__(self, *, custom_integration, integration, module, relative_filename, frame) -> None: ...

def get_integration_logger(fallback_name: str) -> logging.Logger: ...
def get_current_frame(depth: int = 0) -> FrameType: ...
def get_integration_frame(exclude_integrations: set | None = None) -> IntegrationFrame: ...

class MissingIntegrationFrame(HomeAssistantError): ...

def report(what: str, exclude_integrations: set | None = None, error_if_core: bool = True, level: int = ..., log_custom_component_only: bool = False, error_if_integration: bool = False) -> None: ...
def _report_integration(what: str, integration_frame: IntegrationFrame, level: int = ..., error: bool = False) -> None: ...
def warn_use(func: _CallableT, what: str) -> _CallableT: ...
