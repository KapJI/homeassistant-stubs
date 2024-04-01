from .const import CONF_ASSOCIATION_DATA as CONF_ASSOCIATION_DATA, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak, async_discovered_service_info as async_discovered_service_info, async_last_service_info as async_last_service_info
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS
from typing import Any

_LOGGER: Incomplete
STEP_ASSOCIATE_SCHEMA: Incomplete

class DormkabaConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _reauth_entry: ConfigEntry | None
    _lock: Incomplete
    _discovered_devices: Incomplete
    _discovery_info: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfoBleak) -> ConfigFlowResult: ...
    async def async_step_bluetooth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_associate(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
