from . import get_api as get_api
from .const import CONF_LIMIT as CONF_LIMIT, CONF_ORDER as CONF_ORDER, DEFAULT_LIMIT as DEFAULT_LIMIT, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_ORDER as DEFAULT_ORDER, DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN, SUPPORTED_ORDER_MODES as SUPPORTED_ORDER_MODES
from .errors import AuthenticationError as AuthenticationError, CannotConnect as CannotConnect, UnknownError as UnknownError
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

DATA_SCHEMA: Incomplete

class TransmissionFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    _reauth_entry: config_entries.ConfigEntry | None
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> TransmissionOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, str] | None = ...) -> FlowResult: ...

class TransmissionOptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
