from _typeshed import Incomplete
from aiohttp import web as web
from homeassistant import config_entries as config_entries, data_entry_flow as data_entry_flow
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.components.http.data_validator import RequestDataValidator as RequestDataValidator
from typing import Any

class _BaseFlowManagerView(HomeAssistantView):
    _flow_mgr: Incomplete
    def __init__(self, flow_mgr: data_entry_flow.FlowManager) -> None: ...
    def _prepare_result_json(self, result: data_entry_flow.FlowResult) -> data_entry_flow.FlowResult: ...

class FlowManagerIndexView(_BaseFlowManagerView):
    async def post(self, request: web.Request, data: dict[str, Any]) -> web.Response: ...

class FlowManagerResourceView(_BaseFlowManagerView):
    async def get(self, request: web.Request, flow_id: str) -> web.Response: ...
    async def post(self, request: web.Request, data: dict[str, Any], flow_id: str) -> web.Response: ...
    async def delete(self, request: web.Request, flow_id: str) -> web.Response: ...
