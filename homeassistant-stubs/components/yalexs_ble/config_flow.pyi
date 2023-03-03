from .const import CONF_KEY as CONF_KEY, CONF_LOCAL_NAME as CONF_LOCAL_NAME, CONF_SLOT as CONF_SLOT, DOMAIN as DOMAIN
from .util import async_find_existing_service_info as async_find_existing_service_info, human_readable_name as human_readable_name
from _typeshed import Incomplete
from bleak_retry_connector import BLEDevice as BLEDevice
from collections.abc import Mapping
from homeassistant import config_entries as config_entries, data_entry_flow as data_entry_flow
from homeassistant.components.bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak, async_ble_device_from_address as async_ble_device_from_address, async_discovered_service_info as async_discovered_service_info
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS
from homeassistant.data_entry_flow import AbortFlow as AbortFlow, FlowResult as FlowResult
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete

async def async_validate_lock_or_error(local_name: str, device: BLEDevice, key: str, slot: int) -> dict[str, str]: ...

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    _discovery_info: Incomplete
    _discovered_devices: Incomplete
    _lock_cfg: Incomplete
    _reauth_entry: Incomplete
    def __init__(self) -> None: ...
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfoBleak) -> FlowResult: ...
    async def async_step_integration_discovery(self, discovery_info: DiscoveryInfoType) -> FlowResult: ...
    async def async_step_integration_discovery_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_validate(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...