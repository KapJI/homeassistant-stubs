from .const import CONF_FW_VERSION as CONF_FW_VERSION, DOMAIN as DOMAIN
from _typeshed import Incomplete
from aio_wattwaechter.models import SystemInfo as SystemInfo
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_MODEL as CONF_MODEL, CONF_TOKEN as CONF_TOKEN
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from typing import Any, override

_LOGGER: Incomplete

class WattwaechterConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _host: str
    _device_id: str
    _model: str | None
    _fw_version: str | None
    _mac: str
    _device_name: str | None
    def __init__(self) -> None: ...
    async def _async_test_connection(self, host: str, token: str | None = None) -> tuple[dict[str, str], SystemInfo | None, str | None]: ...
    def _create_entry(self, token: str | None = None) -> ConfigFlowResult: ...
    @override
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_auth(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
