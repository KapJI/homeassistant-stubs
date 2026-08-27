from .const import FlowType as FlowType
from collections.abc import Mapping
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlowResult as ConfigFlowResult, SubentryFlowResult as SubentryFlowResult
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any, Protocol, override

class RepairsFlowResult(data_entry_flow.FlowResult[data_entry_flow.FlowContext, str], total=False):
    next_flow: tuple[FlowType, str]
    result: ConfigEntry | None

class RepairsFlow(data_entry_flow.FlowHandler[data_entry_flow.FlowContext, RepairsFlowResult, str]):
    issue_id: str
    data: dict[str, str | int | float | None] | None
    @override
    @callback
    def async_create_entry(self, *, title: str | None = None, data: Mapping[str, Any], description: str | None = None, description_placeholders: Mapping[str, str] | None = None, next_flow: tuple[FlowType, str] | None = None) -> RepairsFlowResult: ...
    @override
    @callback
    def async_abort(self, *, reason: str, description_placeholders: Mapping[str, str] | None = None, translation_domain: str | None = None, next_flow: tuple[FlowType, str] | None = None) -> RepairsFlowResult: ...
    @callback
    def _async_set_next_flow_if_valid(self, result: RepairsFlowResult, next_flow: tuple[FlowType, str] | None) -> None: ...

class RepairsProtocol(Protocol):
    async def async_create_fix_flow(self, hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...
