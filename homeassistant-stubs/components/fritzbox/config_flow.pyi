from .const import DEFAULT_HOST as DEFAULT_HOST, DEFAULT_USERNAME as DEFAULT_USERNAME, DOMAIN as DOMAIN
from homeassistant.components import ssdp as ssdp
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

DATA_SCHEMA_USER: Any
DATA_SCHEMA_CONFIRM: Any
RESULT_INVALID_AUTH: str
RESULT_NO_DEVICES_FOUND: str
RESULT_NOT_SUPPORTED: str
RESULT_SUCCESS: str

class FritzboxConfigFlow(ConfigFlow):
    VERSION: int
    _entry: Any
    _host: Any
    _name: Any
    _password: Any
    _username: Any
    def __init__(self) -> None: ...
    def _get_entry(self, name: str) -> FlowResult: ...
    async def _update_entry(self) -> None: ...
    def _try_connect(self) -> str: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> FlowResult: ...
    async def async_step_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_reauth(self, data: dict[str, str]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
