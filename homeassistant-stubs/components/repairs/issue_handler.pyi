from .const import DOMAIN as DOMAIN
from .models import RepairsFlow as RepairsFlow, RepairsFlowContext as RepairsFlowContext, RepairsFlowResult as RepairsFlowResult, RepairsProtocol as RepairsProtocol
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.integration_platform import LazyIntegrationPlatforms as LazyIntegrationPlatforms
from typing import Any, override

class ConfirmRepairFlow(RepairsFlow):
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> RepairsFlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, str] | None = None) -> RepairsFlowResult: ...

class RepairsFlowManager(data_entry_flow.FlowManager[RepairsFlowContext, RepairsFlowResult, str]):
    @override
    async def async_init(self, handler: str, *, context: RepairsFlowContext | None = None, data: dict[str, Any] | None = None) -> RepairsFlowResult: ...
    @override
    async def async_create_flow(self, handler_key: str, *, context: RepairsFlowContext | None = None, data: dict[str, Any] | None = None) -> RepairsFlow: ...
    @override
    async def async_finish_flow(self, flow: data_entry_flow.FlowHandler[RepairsFlowContext, RepairsFlowResult, str], result: RepairsFlowResult) -> RepairsFlowResult: ...

@callback
def async_setup(hass: HomeAssistant) -> None: ...
@callback
def _process_repairs_platform(hass: HomeAssistant, integration_domain: str, platform: RepairsProtocol) -> RepairsProtocol: ...
