from .const import STATE_POLL_INTERVAL as STATE_POLL_INTERVAL
from _typeshed import Incomplete
from homeassistant.components.bluetooth import BluetoothChange as BluetoothChange, BluetoothScanningMode as BluetoothScanningMode, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from homeassistant.components.bluetooth.active_update_coordinator import ActiveBluetoothDataUpdateCoordinator as ActiveBluetoothDataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from pycasperglow import CasperGlow as CasperGlow

_LOGGER: Incomplete
type CasperGlowConfigEntry = ConfigEntry[CasperGlowCoordinator]

class CasperGlowCoordinator(ActiveBluetoothDataUpdateCoordinator[None]):
    device: Incomplete
    last_dimming_time_minutes: int | None
    title: Incomplete
    def __init__(self, hass: HomeAssistant, device: CasperGlow, title: str) -> None: ...
    @callback
    def _needs_poll(self, service_info: BluetoothServiceInfoBleak, seconds_since_last_poll: float | None) -> bool: ...
    async def _async_update(self, service_info: BluetoothServiceInfoBleak) -> None: ...
    last_poll_successful: bool
    _last_poll: Incomplete
    async def _async_poll(self) -> None: ...
    @callback
    def _async_handle_bluetooth_event(self, service_info: BluetoothServiceInfoBleak, change: BluetoothChange) -> None: ...
