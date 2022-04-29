from .const import CONF_DNSMASQ as CONF_DNSMASQ, CONF_INTERFACE as CONF_INTERFACE, CONF_REQUIRE_IP as CONF_REQUIRE_IP, CONF_SSH_KEY as CONF_SSH_KEY, CONF_TRACK_UNKNOWN as CONF_TRACK_UNKNOWN, DEFAULT_DNSMASQ as DEFAULT_DNSMASQ, DEFAULT_INTERFACE as DEFAULT_INTERFACE, DEFAULT_TRACK_UNKNOWN as DEFAULT_TRACK_UNKNOWN, DOMAIN as DOMAIN, MODE_AP as MODE_AP, MODE_ROUTER as MODE_ROUTER, PROTOCOL_SSH as PROTOCOL_SSH, PROTOCOL_TELNET as PROTOCOL_TELNET
from .router import get_api as get_api
from _typeshed import Incomplete
from homeassistant.components.device_tracker.const import CONF_CONSIDER_HOME as CONF_CONSIDER_HOME, DEFAULT_CONSIDER_HOME as DEFAULT_CONSIDER_HOME
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MODE as CONF_MODE, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_PROTOCOL as CONF_PROTOCOL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

RESULT_CONN_ERROR: str
RESULT_UNKNOWN: str
RESULT_SUCCESS: str
_LOGGER: Incomplete

def _is_file(value: str) -> bool: ...
def _get_ip(host: str) -> Union[str, None]: ...

class AsusWrtFlowHandler(ConfigFlow):
    VERSION: int
    def _show_setup_form(self, user_input: Union[dict[str, Any], None] = ..., errors: Union[dict[str, str], None] = ...) -> FlowResult: ...
    @staticmethod
    async def _async_check_connection(user_input: dict[str, Any]) -> str: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...

class OptionsFlowHandler(OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
