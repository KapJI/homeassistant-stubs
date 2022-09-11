from _typeshed import Incomplete
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

WS_TYPE_SETUP_MFA: str
SCHEMA_WS_SETUP_MFA: Incomplete
WS_TYPE_DEPOSE_MFA: str
SCHEMA_WS_DEPOSE_MFA: Incomplete
DATA_SETUP_FLOW_MGR: str
_LOGGER: Incomplete

class MfaFlowManager(data_entry_flow.FlowManager):
    async def async_create_flow(self, handler_key: Any, *, context: dict[str, Any], data: dict[str, Any]) -> data_entry_flow.FlowHandler: ...
    async def async_finish_flow(self, flow: data_entry_flow.FlowHandler, result: data_entry_flow.FlowResult) -> data_entry_flow.FlowResult: ...

async def async_setup(hass: HomeAssistant) -> None: ...
def websocket_setup_mfa(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def websocket_depose_mfa(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def _prepare_result_json(result: data_entry_flow.FlowResult) -> data_entry_flow.FlowResult: ...
