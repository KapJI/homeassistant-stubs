import voluptuous as vol
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from bleak.backends.device import BLEDevice as BLEDevice
from homeassistant import config_entries as config_entries
from homeassistant.components import bluetooth as bluetooth
from homeassistant.components.bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak, async_discovered_service_info as async_discovered_service_info
from homeassistant.config_entries import ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_NAME as CONF_NAME, CONF_PIN as CONF_PIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import selector as selector
from typing import Any, override

_LOGGER: Incomplete

def _normalize_address(address: str) -> str: ...

PIN_SCHEMA: Incomplete
PIN_ONLY_SCHEMA: Incomplete

def _user_schema(discoveries: dict[str, BluetoothServiceInfoBleak]) -> vol.Schema: ...
async def _async_validate_input(hass: HomeAssistant, *, address: str, pin: str, name: str | None) -> str: ...

class BesenConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovered_address: str | None
    _discovered_name: str | None
    _discovered_devices: dict[str, BluetoothServiceInfoBleak]
    def __init__(self) -> None: ...
    @override
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfoBleak) -> ConfigFlowResult: ...
    async def async_step_bluetooth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
