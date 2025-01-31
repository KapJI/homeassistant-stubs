from .const import CONF_API_TYPE as CONF_API_TYPE, CONF_HUB as CONF_HUB, DEFAULT_SERVER as DEFAULT_SERVER, DOMAIN as DOMAIN, LOGGER as LOGGER
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from homeassistant.helpers.service_info.dhcp import DhcpServiceInfo as DhcpServiceInfo
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from pyoverkiz.client import OverkizClient
from pyoverkiz.enums import APIType
from pyoverkiz.models import OverkizServer as OverkizServer
from typing import Any

class DeveloperModeDisabled(HomeAssistantError): ...

class OverkizConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _api_type: APIType
    _user: str | None
    _server: str
    _host: str
    async def async_validate_input(self, user_input: dict[str, Any]) -> dict[str, Any]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_local_or_cloud(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_cloud(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_local(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def _process_discovery(self, gateway_id: str) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    def _create_cloud_client(self, username: str, password: str, server: OverkizServer) -> OverkizClient: ...
    async def _create_local_api_token(self, cloud_client: OverkizClient, host: str, verify_ssl: bool) -> str: ...
