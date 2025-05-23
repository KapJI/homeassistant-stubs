from aiohttp import web
from collections.abc import Callable as Callable
from homeassistant import config_entries as config_entries, data_entry_flow as data_entry_flow
from homeassistant.auth.permissions.const import CAT_CONFIG_ENTRIES as CAT_CONFIG_ENTRIES, POLICY_EDIT as POLICY_EDIT
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS, require_admin as require_admin
from homeassistant.components.http.data_validator import RequestDataValidator as RequestDataValidator
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import DependencyError as DependencyError, Unauthorized as Unauthorized
from homeassistant.helpers.data_entry_flow import FlowManagerIndexView as FlowManagerIndexView, FlowManagerResourceView as FlowManagerResourceView
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.json import json_fragment as json_fragment
from homeassistant.loader import Integration as Integration, IntegrationNotFound as IntegrationNotFound, async_get_config_flows as async_get_config_flows, async_get_integrations as async_get_integrations, async_get_loaded_integration as async_get_loaded_integration
from typing import Any, NoReturn

@callback
def async_setup(hass: HomeAssistant) -> bool: ...

class ConfigManagerEntryIndexView(HomeAssistantView):
    url: str
    name: str
    async def get(self, request: web.Request) -> web.Response: ...

class ConfigManagerEntryResourceView(HomeAssistantView):
    url: str
    name: str
    async def delete(self, request: web.Request, entry_id: str) -> web.Response: ...

class ConfigManagerEntryResourceReloadView(HomeAssistantView):
    url: str
    name: str
    async def post(self, request: web.Request, entry_id: str) -> web.Response: ...

def _prepare_config_flow_result_json(result: data_entry_flow.FlowResult, prepare_result_json: Callable[[data_entry_flow.FlowResult], data_entry_flow.FlowResult]) -> data_entry_flow.FlowResult: ...

class ConfigManagerFlowIndexView(FlowManagerIndexView[config_entries.ConfigEntriesFlowManager]):
    url: str
    name: str
    async def get(self, request: web.Request) -> NoReturn: ...
    async def post(self, request: web.Request, data: dict[str, Any]) -> web.Response: ...
    async def _post_impl(self, request: web.Request, data: dict[str, Any]) -> web.Response: ...
    def get_context(self, data: dict[str, Any]) -> dict[str, Any]: ...
    def _prepare_result_json(self, result: data_entry_flow.FlowResult) -> data_entry_flow.FlowResult: ...

class ConfigManagerFlowResourceView(FlowManagerResourceView[config_entries.ConfigEntriesFlowManager]):
    url: str
    name: str
    async def get(self, request: web.Request, /, flow_id: str) -> web.Response: ...
    async def post(self, request: web.Request, flow_id: str) -> web.Response: ...
    def _prepare_result_json(self, result: data_entry_flow.FlowResult) -> data_entry_flow.FlowResult: ...

class ConfigManagerAvailableFlowView(HomeAssistantView):
    url: str
    name: str
    async def get(self, request: web.Request) -> web.Response: ...

class OptionManagerFlowIndexView(FlowManagerIndexView[config_entries.OptionsFlowManager]):
    url: str
    name: str
    async def post(self, request: web.Request) -> web.Response: ...

class OptionManagerFlowResourceView(FlowManagerResourceView[config_entries.OptionsFlowManager]):
    url: str
    name: str
    async def get(self, request: web.Request, /, flow_id: str) -> web.Response: ...
    async def post(self, request: web.Request, flow_id: str) -> web.Response: ...

class SubentryManagerFlowIndexView(FlowManagerIndexView[config_entries.ConfigSubentryFlowManager]):
    url: str
    name: str
    async def post(self, request: web.Request, data: dict[str, Any]) -> web.Response: ...
    def get_context(self, data: dict[str, Any]) -> dict[str, Any]: ...

class SubentryManagerFlowResourceView(FlowManagerResourceView[config_entries.ConfigSubentryFlowManager]):
    url: str
    name: str
    async def get(self, request: web.Request, /, flow_id: str) -> web.Response: ...
    async def post(self, request: web.Request, flow_id: str) -> web.Response: ...

@websocket_api.require_admin
def config_entries_flow_progress(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
def config_entries_flow_subscribe(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def send_entry_not_found(connection: websocket_api.ActiveConnection, msg_id: int) -> None: ...
def get_entry(hass: HomeAssistant, connection: websocket_api.ActiveConnection, entry_id: str, msg_id: int) -> config_entries.ConfigEntry | None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def config_entry_get_single(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def config_entry_update(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def config_entry_disable(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def ignore_config_flow(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def config_entries_get(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def config_entries_subscribe(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
async def _async_matching_config_entries_json_fragments(hass: HomeAssistant, type_filter: list[str] | None, domain: str | None) -> list[json_fragment]: ...
@websocket_api.require_admin
@websocket_api.async_response
async def config_subentry_list(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def config_subentry_delete(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
