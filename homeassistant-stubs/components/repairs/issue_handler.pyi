from .const import DOMAIN as DOMAIN
from .models import RepairsFlow as RepairsFlow, RepairsProtocol as RepairsProtocol
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.integration_platform import async_process_integration_platforms as async_process_integration_platforms
from typing import Any

class ConfirmRepairFlow(RepairsFlow):
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> data_entry_flow.FlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, str] | None = None) -> data_entry_flow.FlowResult: ...

class RepairsFlowManager(data_entry_flow.FlowManager):
    async def async_create_flow(self, handler_key: str, *, context: data_entry_flow.FlowContext | None = None, data: dict[str, Any] | None = None) -> RepairsFlow: ...
    async def async_finish_flow(self, flow: data_entry_flow.FlowHandler, result: data_entry_flow.FlowResult) -> data_entry_flow.FlowResult: ...

@callback
def async_setup(hass: HomeAssistant) -> None: ...
async def async_process_repairs_platforms(hass: HomeAssistant) -> None: ...
@callback
def _register_repairs_platform(hass: HomeAssistant, integration_domain: str, platform: RepairsProtocol) -> None: ...
