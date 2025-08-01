from .const import CONF_MANUFACTURER as CONF_MANUFACTURER, CONF_TRACK_WIRED_CLIENTS as CONF_TRACK_WIRED_CLIENTS, CONF_UNAUTHENTICATED_MODE as CONF_UNAUTHENTICATED_MODE, CONF_UPNP_UDN as CONF_UPNP_UDN, CONNECTION_TIMEOUT as CONNECTION_TIMEOUT, DEFAULT_DEVICE_NAME as DEFAULT_DEVICE_NAME, DEFAULT_NOTIFY_SERVICE_NAME as DEFAULT_NOTIFY_SERVICE_NAME, DEFAULT_TRACK_WIRED_CLIENTS as DEFAULT_TRACK_WIRED_CLIENTS, DEFAULT_UNAUTHENTICATED_MODE as DEFAULT_UNAUTHENTICATED_MODE, DOMAIN as DOMAIN
from .utils import get_device_macs as get_device_macs, non_verifying_requests_session as non_verifying_requests_session
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_MAC as CONF_MAC, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_RECIPIENT as CONF_RECIPIENT, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import callback as callback
from homeassistant.helpers.service_info.ssdp import ATTR_UPNP_FRIENDLY_NAME as ATTR_UPNP_FRIENDLY_NAME, ATTR_UPNP_MANUFACTURER as ATTR_UPNP_MANUFACTURER, ATTR_UPNP_MODEL_NAME as ATTR_UPNP_MODEL_NAME, ATTR_UPNP_PRESENTATION_URL as ATTR_UPNP_PRESENTATION_URL, ATTR_UPNP_SERIAL as ATTR_UPNP_SERIAL, ATTR_UPNP_UDN as ATTR_UPNP_UDN, SsdpServiceInfo as SsdpServiceInfo
from huawei_lte_api.Connection import Connection
from huawei_lte_api.Session import GetResponseType as GetResponseType
from typing import Any

_LOGGER: Incomplete

class HuaweiLteConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    manufacturer: str | None
    upnp_udn: str | None
    url: str | None
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> HuaweiLteOptionsFlow: ...
    async def _async_show_user_form(self, user_input: dict[str, Any] | None = None, errors: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def _async_show_reauth_form(self, user_input: dict[str, Any], errors: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def _connect(self, user_input: dict[str, Any], errors: dict[str, str]) -> Connection | None: ...
    @staticmethod
    def _disconnect(conn: Connection) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_ssdp(self, discovery_info: SsdpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class HuaweiLteOptionsFlow(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
