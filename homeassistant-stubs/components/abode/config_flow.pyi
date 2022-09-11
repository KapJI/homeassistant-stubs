from .const import CONF_POLLING as CONF_POLLING, DEFAULT_CACHEDB as DEFAULT_CACHEDB, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

CONF_MFA: str

class AbodeFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    data_schema: Incomplete
    mfa_data_schema: Incomplete
    _cache: Incomplete
    _mfa_code: Incomplete
    _password: Incomplete
    _polling: bool
    _username: Incomplete
    def __init__(self) -> None: ...
    async def _async_abode_login(self, step_id: str) -> FlowResult: ...
    async def _async_abode_mfa_login(self) -> FlowResult: ...
    async def _async_create_entry(self) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_mfa(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
