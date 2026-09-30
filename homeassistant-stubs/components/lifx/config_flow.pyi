from .const import CONF_SERIAL as CONF_SERIAL, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import LIFXConfigEntry as LIFXConfigEntry
from .discovery import async_discover_devices as async_discover_devices
from .util import async_entry_serial as async_entry_serial, async_resolve_host as async_resolve_host, normalize_serial as normalize_serial
from dataclasses import dataclass
from homeassistant.components import onboarding as onboarding
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_HOST as CONF_HOST
from homeassistant.core import callback as callback
from homeassistant.helpers.service_info.dhcp import DhcpServiceInfo as DhcpServiceInfo
from homeassistant.helpers.service_info.zeroconf import ATTR_PROPERTIES_ID as ATTR_PROPERTIES_ID, ZeroconfServiceInfo as ZeroconfServiceInfo
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from lifx import DiscoveredDevice as DiscoveredDevice
from typing import Any, Self, override

@dataclass(slots=True)
class FlowDevice:
    ip: str
    serial: str
    label: str
    group: str

class LIFXConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    host: str | None
    _discovered_devices: dict[str, DiscoveredDevice]
    _discovered_device: FlowDevice | None
    def __init__(self) -> None: ...
    async def _async_set_serial_and_repair(self, raw_serial: str, host: str, raise_on_progress: bool = True) -> None: ...
    @override
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    @override
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    @callback
    def _async_abort_configured_entry(self, entry: LIFXConfigEntry, host: str) -> ConfigFlowResult: ...
    @override
    async def async_step_homekit(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    @override
    async def async_step_integration_discovery(self, discovery_info: DiscoveryInfoType) -> ConfigFlowResult: ...
    async def _async_handle_discovery(self, host: str, serial: str | None = None) -> ConfigFlowResult: ...
    @override
    def is_matching(self, other_flow: Self) -> bool: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_pick_device(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @callback
    def _async_create_entry_from_device(self, device: FlowDevice) -> ConfigFlowResult: ...
    async def _async_try_connect(self, host: str | None, serial: str | None = None) -> FlowDevice | None: ...
