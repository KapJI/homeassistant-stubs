from _typeshed import Incomplete
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Protocol

RepairsFlowResult: Incomplete

class RepairsFlow(data_entry_flow.FlowHandler[data_entry_flow.FlowContext, RepairsFlowResult, str]):
    issue_id: str
    data: dict[str, str | int | float | None] | None

class RepairsProtocol(Protocol):
    async def async_create_fix_flow(self, hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...
