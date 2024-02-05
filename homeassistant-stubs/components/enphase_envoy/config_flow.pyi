import voluptuous as vol
from .const import DOMAIN as DOMAIN, INVALID_AUTH_ERRORS as INVALID_AUTH_ERRORS
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.components import zeroconf as zeroconf
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from pyenphase import Envoy
from typing import Any

_LOGGER: Incomplete
ENVOY: str
CONF_SERIAL: str
INSTALLER_AUTH_USERNAME: str

async def validate_input(hass: HomeAssistant, host: str, username: str, password: str) -> Envoy: ...

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    ip_address: Incomplete
    username: Incomplete
    protovers: Incomplete
    _reauth_entry: Incomplete
    def __init__(self) -> None: ...
    def _async_generate_schema(self) -> vol.Schema: ...
    def _async_current_hosts(self) -> set[str]: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    def _async_envoy_name(self) -> str: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
