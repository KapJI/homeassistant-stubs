from .const import CONF_ALLOW_CLIP_SENSOR as CONF_ALLOW_CLIP_SENSOR, CONF_ALLOW_DECONZ_GROUPS as CONF_ALLOW_DECONZ_GROUPS, CONF_ALLOW_NEW_DEVICES as CONF_ALLOW_NEW_DEVICES, DEFAULT_ALLOW_CLIP_SENSOR as DEFAULT_ALLOW_CLIP_SENSOR, DEFAULT_ALLOW_DECONZ_GROUPS as DEFAULT_ALLOW_DECONZ_GROUPS, DEFAULT_ALLOW_NEW_DEVICES as DEFAULT_ALLOW_NEW_DEVICES, DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN, HASSIO_CONFIGURATION_URL as HASSIO_CONFIGURATION_URL, LOGGER as LOGGER
from .gateway import DeconzGateway as DeconzGateway
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.components import ssdp as ssdp
from homeassistant.components.hassio import HassioServiceInfo as HassioServiceInfo
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from pydeconz.utils import DiscoveredBridge as DiscoveredBridge
from typing import Any

DECONZ_MANUFACTURERURL: str
CONF_SERIAL: str
CONF_MANUAL_INPUT: str

def get_master_gateway(hass: HomeAssistant) -> DeconzGateway: ...

class DeconzFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _hassio_discovery: dict[str, Any]
    bridges: list[DiscoveredBridge]
    host: str
    port: int
    api_key: str
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...
    bridge_id: str
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_manual_input(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_link(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def _create_entry(self) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> FlowResult: ...
    async def async_step_hassio(self, discovery_info: HassioServiceInfo) -> FlowResult: ...
    async def async_step_hassio_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...

class DeconzOptionsFlowHandler(OptionsFlow):
    gateway: DeconzGateway
    config_entry: Incomplete
    options: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_deconz_devices(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
