from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Generator
from homeassistant.components.trace import ActionTrace as ActionTrace, async_store_trace as async_store_trace
from homeassistant.components.trace.const import CONF_STORED_TRACES as CONF_STORED_TRACES
from homeassistant.core import Context as Context
from typing import Any

class AutomationTrace(ActionTrace):
    _domain: Incomplete
    _trigger_description: Incomplete
    def __init__(self, item_id: str, config: dict[str, Any], blueprint_inputs: dict[str, Any], context: Context) -> None: ...
    def set_trigger_description(self, trigger: str) -> None: ...
    def as_short_dict(self) -> dict[str, Any]: ...

def trace_automation(hass, automation_id, config, blueprint_inputs, context, trace_config) -> Generator[Incomplete, None, None]: ...
