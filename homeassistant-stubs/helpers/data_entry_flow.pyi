from aiohttp import web as web
from homeassistant import config_entries as config_entries, data_entry_flow as data_entry_flow
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.components.http.data_validator import RequestDataValidator as RequestDataValidator
from homeassistant.const import HTTP_BAD_REQUEST as HTTP_BAD_REQUEST, HTTP_NOT_FOUND as HTTP_NOT_FOUND
from typing import Any

class _BaseFlowManagerView(HomeAssistantView):
    def __init__(self, flow_mgr: data_entry_flow.FlowManager) -> None: ...

class FlowManagerIndexView(_BaseFlowManagerView):
    async def post(self, request: web.Request, data: dict[str, Any]) -> web.Response: ...

class FlowManagerResourceView(_BaseFlowManagerView):
    async def get(self, request: web.Request, flow_id: str) -> web.Response: ...
    async def post(self, request: web.Request, flow_id: str, data: dict[str, Any]) -> web.Response: ...
    async def delete(self, request: web.Request, flow_id: str) -> web.Response: ...
