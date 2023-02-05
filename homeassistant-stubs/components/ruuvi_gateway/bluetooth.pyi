from .coordinator import RuuviGatewayUpdateCoordinator as RuuviGatewayUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from home_assistant_bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from homeassistant.components.bluetooth import BaseHaRemoteScanner as BaseHaRemoteScanner, FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS as FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS, async_get_advertisement_callback as async_get_advertisement_callback, async_register_scanner as async_register_scanner
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback

_LOGGER: Incomplete

class RuuviGatewayScanner(BaseHaRemoteScanner):
    coordinator: Incomplete
    def __init__(self, hass: HomeAssistant, scanner_id: str, name: str, new_info_callback: Callable[[BluetoothServiceInfoBleak], None], *, coordinator: RuuviGatewayUpdateCoordinator) -> None: ...
    def _async_handle_new_data(self) -> None: ...
    def start_polling(self) -> CALLBACK_TYPE: ...

def async_connect_scanner(hass: HomeAssistant, entry: ConfigEntry, coordinator: RuuviGatewayUpdateCoordinator) -> tuple[RuuviGatewayScanner, CALLBACK_TYPE]: ...
