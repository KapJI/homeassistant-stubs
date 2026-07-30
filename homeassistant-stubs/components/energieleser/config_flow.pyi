from .const import CONF_SW_VERSION as CONF_SW_VERSION, DOMAIN as DOMAIN, device_model_name as device_model_name
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_HOST as CONF_HOST
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import TextSelector as TextSelector
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from typing import Any, override

STEP_USER_SCHEMA: Incomplete

class EnergieleserConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovered_host: str
    _discovered_device_id: str
    _discovered_device_type: str
    _discovered_sw_version: str | None
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    def _create_entry(self, host: str, title: str, device_id: str, sw_version: str | None = None) -> ConfigFlowResult: ...
