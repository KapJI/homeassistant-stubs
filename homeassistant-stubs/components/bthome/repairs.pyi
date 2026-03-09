from . import get_encryption_issue_id as get_encryption_issue_id
from .const import CONF_BINDKEY as CONF_BINDKEY, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.components.repairs import RepairsFlow as RepairsFlow
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

class EncryptionRemovedRepairFlow(RepairsFlow):
    _entry_id: Incomplete
    _entry_title: Incomplete
    def __init__(self, entry_id: str, entry_title: str) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> data_entry_flow.FlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, Any] | None = None) -> data_entry_flow.FlowResult: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, Any] | None) -> RepairsFlow: ...
