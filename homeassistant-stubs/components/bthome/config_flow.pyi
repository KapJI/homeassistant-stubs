import dataclasses
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from bthome_ble import BTHomeBluetoothDeviceData as DeviceData
from collections.abc import Mapping
from homeassistant.components import onboarding as onboarding
from homeassistant.components.bluetooth import BluetoothServiceInfo as BluetoothServiceInfo, async_discovered_service_info as async_discovered_service_info
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

@dataclasses.dataclass
class Discovery:
    title: str
    discovery_info: BluetoothServiceInfo
    device: DeviceData
    def __init__(self, title, discovery_info, device) -> None: ...

def _title(discovery_info: BluetoothServiceInfo, device: DeviceData) -> str: ...

class BTHomeConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovery_info: Incomplete
    _discovered_device: Incomplete
    _discovered_devices: Incomplete
    def __init__(self) -> None: ...
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfo) -> FlowResult: ...
    async def async_step_get_encryption_key(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_bluetooth_confirm(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    def _async_get_or_create_entry(self, bindkey: str | None = None) -> FlowResult: ...
