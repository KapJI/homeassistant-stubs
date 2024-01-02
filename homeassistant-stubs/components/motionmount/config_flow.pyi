from .const import DOMAIN as DOMAIN, EMPTY_MAC as EMPTY_MAC
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components import zeroconf as zeroconf
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, CONF_UUID as CONF_UUID
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.device_registry import format_mac as format_mac
from typing import Any

_LOGGER: Incomplete

class MotionMountFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    discovery_info: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def _validate_input(self, data: dict) -> dict[str, Any]: ...
    def _show_setup_form(self, errors: dict[str, str] | None = None) -> FlowResult: ...
