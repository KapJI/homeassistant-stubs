from . import create_hyperion_client as create_hyperion_client
from .const import CONF_AUTH_ID as CONF_AUTH_ID, CONF_CREATE_TOKEN as CONF_CREATE_TOKEN, CONF_EFFECT_HIDE_LIST as CONF_EFFECT_HIDE_LIST, CONF_EFFECT_SHOW_LIST as CONF_EFFECT_SHOW_LIST, CONF_PRIORITY as CONF_PRIORITY, DEFAULT_ORIGIN as DEFAULT_ORIGIN, DEFAULT_PRIORITY as DEFAULT_PRIORITY, DOMAIN as DOMAIN
from homeassistant.components.ssdp import ATTR_SSDP_LOCATION as ATTR_SSDP_LOCATION, ATTR_UPNP_SERIAL as ATTR_UPNP_SERIAL
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, OptionsFlow as OptionsFlow, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_BASE as CONF_BASE, CONF_HOST as CONF_HOST, CONF_ID as CONF_ID, CONF_PORT as CONF_PORT, CONF_SOURCE as CONF_SOURCE, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from hyperion import client
from typing import Any

_LOGGER: Any

class HyperionConfigFlow(ConfigFlow):
    VERSION: int
    _data: Any
    _request_token_task: Any
    _auth_id: Any
    _require_confirm: bool
    _port_ui: Any
    def __init__(self) -> None: ...
    def _create_client(self, raw_connection: bool = ...) -> client.HyperionClient: ...
    async def _advance_to_auth_step_if_necessary(self, hyperion_client: client.HyperionClient) -> FlowResult: ...
    async def async_step_reauth(self, config_data: dict[str, Any]) -> FlowResult: ...
    async def async_step_ssdp(self, discovery_info: dict[str, Any]) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _cancel_request_token_task(self) -> None: ...
    async def _request_token_task_func(self, auth_id: str) -> None: ...
    def _get_hyperion_url(self) -> str: ...
    async def _can_login(self) -> Union[bool, None]: ...
    async def async_step_auth(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_create_token(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_create_token_external(self, auth_resp: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_create_token_success(self, _: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_create_token_fail(self, _: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> HyperionOptionsFlow: ...

class HyperionOptionsFlow(OptionsFlow):
    _config_entry: Any
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    def _create_client(self) -> client.HyperionClient: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
