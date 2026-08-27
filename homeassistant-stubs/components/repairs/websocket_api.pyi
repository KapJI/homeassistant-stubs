from .const import DOMAIN as DOMAIN
from .issue_handler import RepairsFlowManager as RepairsFlowManager
from aiohttp import web as web
from collections.abc import Callable as Callable
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.auth.permissions.const import POLICY_EDIT as POLICY_EDIT
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.http.data_validator import RequestDataValidator as RequestDataValidator
from homeassistant.components.http.decorators import require_admin as require_admin
from homeassistant.config_entries import ConfigEntry as ConfigEntry, UnknownEntry as UnknownEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.data_entry_flow import FlowManagerIndexView as FlowManagerIndexView, FlowManagerResourceView as FlowManagerResourceView
from typing import Any, override

@callback
def async_setup(hass: HomeAssistant) -> None: ...
@callback
def ws_get_issue_data(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def ws_ignore_issue(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def ws_list_issues(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def _prepare_repairs_flow_result_json(result: data_entry_flow.FlowResult, prepare_result_json: Callable[[data_entry_flow.FlowResult], dict[str, Any]]) -> dict[str, Any]: ...

class RepairsFlowIndexView(FlowManagerIndexView[RepairsFlowManager]):
    url: str
    name: str
    @override
    async def post(self, request: web.Request, data: dict[str, Any]) -> web.Response: ...
    @override
    def _prepare_result_json(self, result: data_entry_flow.FlowResult) -> dict[str, Any]: ...

class RepairsFlowResourceView(FlowManagerResourceView[RepairsFlowManager]):
    url: str
    name: str
    @override
    async def get(self, request: web.Request, /, flow_id: str) -> web.Response: ...
    @override
    async def post(self, request: web.Request, flow_id: str) -> web.Response: ...
    @override
    def _prepare_result_json(self, result: data_entry_flow.FlowResult) -> dict[str, Any]: ...
