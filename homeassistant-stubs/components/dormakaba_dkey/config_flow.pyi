from .const import CONF_ASSOCIATION_DATA as CONF_ASSOCIATION_DATA, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.components.bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak, async_discovered_service_info as async_discovered_service_info, async_last_service_info as async_last_service_info
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

_LOGGER: Incomplete
STEP_ASSOCIATE_SCHEMA: Incomplete

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    _reauth_entry: config_entries.ConfigEntry | None
    _lock: Incomplete
    _discovered_devices: Incomplete
    _discovery_info: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfoBleak) -> FlowResult: ...
    async def async_step_bluetooth_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_associate(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
