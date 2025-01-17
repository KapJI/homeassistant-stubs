import dataclasses
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components import onboarding as onboarding
from homeassistant.components.bluetooth import BluetoothScanningMode as BluetoothScanningMode, BluetoothServiceInfo as BluetoothServiceInfo, async_discovered_service_info as async_discovered_service_info, async_process_advertisements as async_process_advertisements
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import AbortFlow as AbortFlow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any
from xiaomi_ble import XiaomiBluetoothDeviceData as DeviceData

ADDITIONAL_DISCOVERY_TIMEOUT: int
_LOGGER: Incomplete

@dataclasses.dataclass
class Discovery:
    title: str
    discovery_info: BluetoothServiceInfo
    device: DeviceData

def _title(discovery_info: BluetoothServiceInfo, device: DeviceData) -> str: ...

class XiaomiConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovery_info: BluetoothServiceInfo | None
    _discovered_device: DeviceData | None
    _discovered_devices: dict[str, Discovery]
    def __init__(self) -> None: ...
    async def _async_wait_for_full_advertisement(self, discovery_info: BluetoothServiceInfo, device: DeviceData) -> BluetoothServiceInfo: ...
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfo) -> ConfigFlowResult: ...
    async def async_step_get_encryption_key_legacy(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_get_encryption_key_4_5(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_cloud_auth(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_get_encryption_key_4_5_choose_method(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_bluetooth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_confirm_slow(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    def _async_get_or_create_entry(self, bindkey: str | None = None) -> ConfigFlowResult: ...
