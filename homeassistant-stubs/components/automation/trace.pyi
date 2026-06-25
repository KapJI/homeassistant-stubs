from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager
from homeassistant.components.trace import ActionTrace as ActionTrace, CONF_STORED_TRACES as CONF_STORED_TRACES, async_store_trace as async_store_trace
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, override

class AutomationTrace(ActionTrace):
    _domain = DOMAIN
    _trigger_description: str | None
    not_triggered: Incomplete
    def __init__(self, item_id: str | None, config: ConfigType | None, blueprint_inputs: ConfigType | None, context: Context, *, not_triggered: bool = False) -> None: ...
    def set_trigger_description(self, trigger: str) -> None: ...
    @override
    def as_short_dict(self) -> dict[str, Any]: ...

@contextmanager
def trace_automation(hass: HomeAssistant, automation_id: str | None, config: ConfigType | None, blueprint_inputs: ConfigType | None, context: Context, trace_config: ConfigType, *, not_triggered: bool = False) -> Generator[AutomationTrace]: ...
