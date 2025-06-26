from .const import CONF_HOST as CONF_HOST, DOMAIN as DOMAIN
from _typeshed import Incomplete
from altruistclient import AltruistDeviceModel as AltruistDeviceModel
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from typing import Any

_LOGGER: Incomplete

class AltruistConfigFlow(ConfigFlow, domain=DOMAIN):
    device: AltruistDeviceModel
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
