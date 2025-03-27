import enum
import logging
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.loader import Integration as Integration, async_get_issue_integration as async_get_issue_integration, async_suggest_report_issue as async_suggest_report_issue
from homeassistant.util.async_ import run_callback_threadsafe as run_callback_threadsafe
from propcache.api import cached_property
from types import FrameType

_LOGGER: Incomplete
_REPORTED_INTEGRATIONS: set[str]

class _Hass:
    hass: HomeAssistant | None

_hass: Incomplete

@callback
def async_setup(hass: HomeAssistant) -> None: ...

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

def get_integration_logger(fallback_name: str) -> logging.Logger: ...
def get_current_frame(depth: int = 0) -> FrameType: ...
def get_integration_frame(exclude_integrations: set | None = None) -> IntegrationFrame: ...

class MissingIntegrationFrame(HomeAssistantError): ...

class ReportBehavior(enum.Enum):
    IGNORE = ...
    LOG = ...
    ERROR = ...

def report_usage(what: str, *, breaks_in_ha_version: str | None = None, core_behavior: ReportBehavior = ..., core_integration_behavior: ReportBehavior = ..., custom_integration_behavior: ReportBehavior = ..., exclude_integrations: set[str] | None = None, integration_domain: str | None = None, level: int = ...) -> None: ...
def _report_usage(hass: HomeAssistant, what: str, *, breaks_in_ha_version: str | None, core_behavior: ReportBehavior, core_integration_behavior: ReportBehavior, custom_integration_behavior: ReportBehavior, exclude_integrations: set[str] | None, integration_domain: str | None, level: int) -> None: ...
def _report_usage_integration_domain(hass: HomeAssistant | None, what: str, breaks_in_ha_version: str | None, integration: Integration, core_integration_behavior: ReportBehavior, custom_integration_behavior: ReportBehavior, level: int) -> None: ...
def _report_usage_integration_frame(hass: HomeAssistant, what: str, breaks_in_ha_version: str | None, integration_frame: IntegrationFrame, level: int = ..., error: bool = False) -> None: ...
def _report_usage_no_integration(what: str, core_behavior: ReportBehavior, breaks_in_ha_version: str | None, err: MissingIntegrationFrame | None) -> None: ...
def warn_use[_CallableT: Callable](func: _CallableT, what: str) -> _CallableT: ...
def report_non_thread_safe_operation(what: str) -> None: ...
