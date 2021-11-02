from collections.abc import Coroutine
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any, TypedDict

class SSDPFlow(TypedDict):
    domain: str
    context: dict[str, Any]
    data: dict

class FlowDispatcher:
    hass: Any
    pending_flows: Any
    started: bool
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_start(self, *_: Any) -> None: ...
    def _async_process_pending_flows(self) -> None: ...
    def create(self, flow: SSDPFlow) -> None: ...
    def _init_flow(self, flow: SSDPFlow) -> Coroutine[None, None, FlowResult]: ...
