from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.repairs import ConfirmRepairFlow as ConfirmRepairFlow, RepairsFlow as RepairsFlow, RepairsFlowResult as RepairsFlowResult
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.issue_registry import async_delete_issue as async_delete_issue

class DeprecatedEntityRepairFlow(RepairsFlow):
    _data: Incomplete
    _issue_id: Incomplete
    def __init__(self, issue_id: str, data: dict[str, str | int | float | None]) -> None: ...
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> RepairsFlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, str] | None = None) -> RepairsFlowResult: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...
