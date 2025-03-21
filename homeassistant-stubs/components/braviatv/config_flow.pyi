from .const import ATTR_CID as ATTR_CID, ATTR_MAC as ATTR_MAC, ATTR_MODEL as ATTR_MODEL, CONF_NICKNAME as CONF_NICKNAME, CONF_USE_PSK as CONF_USE_PSK, DOMAIN as DOMAIN, NICKNAME_PREFIX as NICKNAME_PREFIX
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_NAME as CONF_NAME, CONF_PIN as CONF_PIN
from homeassistant.helpers import instance_id as instance_id
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from homeassistant.helpers.service_info.ssdp import ATTR_UPNP_FRIENDLY_NAME as ATTR_UPNP_FRIENDLY_NAME, ATTR_UPNP_MODEL_NAME as ATTR_UPNP_MODEL_NAME, ATTR_UPNP_UDN as ATTR_UPNP_UDN, SsdpServiceInfo as SsdpServiceInfo
from homeassistant.util.network import is_host_valid as is_host_valid
from pybravia import BraviaClient
from typing import Any

class BraviaTVConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    client: BraviaClient | None
    device_config: dict[str, Any]
    def __init__(self) -> None: ...
    def create_client(self) -> None: ...
    async def gen_instance_ids(self) -> tuple[str, str]: ...
    async def async_connect_device(self) -> None: ...
    async def async_create_device(self) -> ConfigFlowResult: ...
    async def async_reauth_device(self) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_authorize(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_pin(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_psk(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_ssdp(self, discovery_info: SsdpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
