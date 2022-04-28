from .const import CONF_GATEWAY_ID as CONF_GATEWAY_ID, CONF_IDENTITY as CONF_IDENTITY, CONF_KEY as CONF_KEY, DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.components import zeroconf as zeroconf
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

KEY_SECURITY_CODE: str

class AuthError(Exception):
    code: Any
    def __init__(self, code: str) -> None: ...

class FlowHandler(config_entries.ConfigFlow):
    VERSION: int
    _host: Any
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_auth(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_homekit(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_import(self, user_input: dict[str, Any]) -> FlowResult: ...
    async def _entry_from_data(self, data: dict[str, Any]) -> FlowResult: ...

async def authenticate(hass: HomeAssistant, host: str, security_code: str) -> dict[str, Union[str, bool]]: ...
async def get_gateway_info(hass: HomeAssistant, host: str, identity: str, key: str) -> dict[str, Union[str, bool]]: ...
