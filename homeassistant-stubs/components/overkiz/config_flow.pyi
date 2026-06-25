import logging
from .const import CONF_API_TYPE as CONF_API_TYPE, CONF_GATEWAY_ID as CONF_GATEWAY_ID, CONF_HUB as CONF_HUB, DEFAULT_SERVER as DEFAULT_SERVER, DOMAIN as DOMAIN, LOGGER as LOGGER
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from homeassistant.helpers.service_info.dhcp import DhcpServiceInfo as DhcpServiceInfo
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from pyoverkiz.client import GatewayCandidate as GatewayCandidate
from pyoverkiz.enums import APIType
from typing import Any, override

LOCAL_API_DOCS_URL: str
TOKEN_DOCS_URL: str

class OverkizConfigFlow(config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN):
    DOMAIN = DOMAIN
    VERSION: int
    MINOR_VERSION: int
    _verify_ssl: bool
    _api_type: APIType
    _user: str | None
    _server: str
    _host: str
    _rexel_gateways: list[GatewayCandidate]
    _rexel_oauth_data: dict[str, Any]
    @property
    @override
    def logger(self) -> logging.Logger: ...
    async def async_validate_input(self, user_input: dict[str, Any]) -> dict[str, Any]: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_local_or_cloud(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_cloud(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_local(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_select_gateway(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_create_rexel_entry(self, gateway: GatewayCandidate) -> ConfigFlowResult: ...
    @override
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    @override
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def _process_discovery(self, gateway_id: str) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
