from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Protocol

class IssueSeverity(StrEnum):
    CRITICAL: str
    ERROR: str
    WARNING: str

class RepairsFlow(data_entry_flow.FlowHandler): ...

class RepairsProtocol(Protocol):
    async def async_create_fix_flow(self, hass: HomeAssistant, issue_id: str) -> RepairsFlow: ...
