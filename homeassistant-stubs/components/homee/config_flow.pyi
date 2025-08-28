from .const import DOMAIN as DOMAIN, RESULT_CANNOT_CONNECT as RESULT_CANNOT_CONNECT, RESULT_INVALID_AUTH as RESULT_INVALID_AUTH, RESULT_UNKNOWN_ERROR as RESULT_UNKNOWN_ERROR
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_USER as SOURCE_USER
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from pyHomee import Homee
from typing import Any

_LOGGER: Incomplete
AUTH_SCHEMA: Incomplete

class HomeeConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    homee: Homee
    _host: str
    _name: str
    _reauth_host: str
    _reauth_username: str
    async def _connect_homee(self) -> dict[str, str]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
