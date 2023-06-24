from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak, async_discovered_service_info as async_discovered_service_info
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class SensirionConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovery_info: Incomplete
    _discovered_device: Incomplete
    _discovered_devices: Incomplete
    def __init__(self) -> None: ...
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfoBleak) -> FlowResult: ...
    async def async_step_bluetooth_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
