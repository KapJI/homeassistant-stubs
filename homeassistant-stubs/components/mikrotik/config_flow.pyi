from .const import CONF_ARP_PING as CONF_ARP_PING, CONF_DETECTION_TIME as CONF_DETECTION_TIME, CONF_FORCE_DHCP as CONF_FORCE_DHCP, DEFAULT_API_PORT as DEFAULT_API_PORT, DEFAULT_DETECTION_TIME as DEFAULT_DETECTION_TIME, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .errors import CannotConnect as CannotConnect, LoginError as LoginError
from .hub import get_api as get_api
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class MikrotikFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    _reauth_entry: Union[config_entries.ConfigEntry, None]
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> MikrotikOptionsFlowHandler: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_reauth(self, data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, str], None] = ...) -> FlowResult: ...

class MikrotikOptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_device_tracker(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
