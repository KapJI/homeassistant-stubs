from .const import CONF_HOST_MANUAL as CONF_HOST_MANUAL, CONF_INFO as CONF_INFO, DOMAIN as DOMAIN
from .discovery import async_discover as async_discover, async_get_discovered_device as async_get_discovered_device
from _typeshed import Incomplete
from aiosenseme import SensemeDevice as SensemeDevice
from homeassistant import config_entries as config_entries
from homeassistant.components import dhcp as dhcp
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_HOST as CONF_HOST, CONF_ID as CONF_ID
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from typing import Any

DISCOVER_TIMEOUT: int

class SensemeFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    _discovered_devices: Incomplete
    _discovered_device: Incomplete
    def __init__(self) -> None: ...
    async def async_step_dhcp(self, discovery_info: dhcp.DhcpServiceInfo) -> FlowResult: ...
    async def async_step_integration_discovery(self, discovery_info: DiscoveryInfoType) -> FlowResult: ...
    async def async_step_discovery_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _async_entry_for_device(self, device: SensemeDevice) -> FlowResult: ...
    async def async_step_manual(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
