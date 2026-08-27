from .const import CONF_PRIV_SCALAR as CONF_PRIV_SCALAR, DEFAULT_USER_SUBTYPE as DEFAULT_USER_SUBTYPE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from cryptography.hazmat.primitives.asymmetric import ec
from homeassistant.components.bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak, async_ble_device_from_address as async_ble_device_from_address, async_discovered_service_info as async_discovered_service_info
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_UUID as CONF_UUID
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any, override

_LOGGER: Incomplete

def _generate_identity() -> ec.EllipticCurvePrivateKey: ...
def _discover_locks(hass: HomeAssistant) -> list[BluetoothServiceInfoBleak]: ...

class IseoConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovered: dict[str, BluetoothServiceInfoBleak]
    _address: str
    _device_name: str
    _uuid_hex: str
    _priv_scalar: str
    _gw_priv: ec.EllipticCurvePrivateKey | None
    def __init__(self) -> None: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfoBleak) -> ConfigFlowResult: ...
    async def async_step_bluetooth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_gw_register(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    def _async_create_iseo_entry(self) -> ConfigFlowResult: ...
