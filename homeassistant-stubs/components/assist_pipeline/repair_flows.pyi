from _typeshed import Incomplete
from homeassistant.components.repairs import RepairsFlow as RepairsFlow, RepairsFlowResult as RepairsFlowResult

REQUIRED_KEYS: Incomplete

class AssistInProgressDeprecatedRepairFlow(RepairsFlow):
    _data: Incomplete
    def __init__(self, data: dict[str, str | int | float | None] | None) -> None: ...
    async def async_step_init(self, _: None = None) -> RepairsFlowResult: ...
    async def async_step_confirm_disable_entity(self, user_input: dict[str, str] | None = None) -> RepairsFlowResult: ...
