from .const import CONF_TOPIC as CONF_TOPIC
from _typeshed import Incomplete
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.components.repairs import ConfirmRepairFlow as ConfirmRepairFlow, RepairsFlow as RepairsFlow
from homeassistant.core import HomeAssistant as HomeAssistant

class TopicProtectedRepairFlow(RepairsFlow):
    entity_id: Incomplete
    topic: Incomplete
    def __init__(self, data: dict[str, str]) -> None: ...
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> data_entry_flow.FlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, str] | None = None) -> data_entry_flow.FlowResult: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, str]) -> RepairsFlow: ...
