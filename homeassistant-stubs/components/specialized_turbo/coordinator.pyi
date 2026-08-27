import logging
from _typeshed import Incomplete
from bleak import BleakClient
from collections.abc import Callable as Callable
from homeassistant.components import bluetooth as bluetooth
from homeassistant.components.bluetooth.active_update_coordinator import ActiveBluetoothDataUpdateCoordinator as ActiveBluetoothDataUpdateCoordinator
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from specialized_turbo import BikeAdvertisement as BikeAdvertisement, BikeInfo as BikeInfo, SpecializedConnection, TelemetryMonitor, TelemetrySnapshot
from typing import override

_POLL_INTERVAL: int

class SpecializedTurboCoordinator(ActiveBluetoothDataUpdateCoordinator[TelemetrySnapshot]):
    _address: Incomplete
    _wrapped_key: Incomplete
    _advertisement: Incomplete
    _bike_info: BikeInfo | None
    _connection: SpecializedConnection | None
    _monitor: TelemetryMonitor | None
    _snapshot: Incomplete
    _reauth_callback: Incomplete
    _reauth_requested: bool
    _poll_lock: Incomplete
    _shutdown_requested: bool
    _was_unavailable: bool
    data: Incomplete
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, *, address: str, wrapped_key: str | None = None, advertisement: BikeAdvertisement | None = None, reauth_callback: Callable[[BikeAdvertisement], None] | None = None) -> None: ...
    @property
    def snapshot(self) -> TelemetrySnapshot: ...
    @callback
    def _needs_poll(self, service_info: bluetooth.BluetoothServiceInfoBleak, seconds_since_last_poll: float | None) -> bool: ...
    async def _do_poll(self, service_info: bluetooth.BluetoothServiceInfoBleak) -> TelemetrySnapshot: ...
    async def _ensure_connected(self, service_info: bluetooth.BluetoothServiceInfoBleak) -> None: ...
    def _update_protocol_metadata(self, service_info: bluetooth.BluetoothServiceInfoBleak) -> None: ...
    def _request_reauth(self) -> None: ...
    def _handle_monitor_update(self, _message: object, snapshot: TelemetrySnapshot) -> None: ...
    @property
    def connected(self) -> bool: ...
    def _on_disconnect(self, _client: BleakClient) -> None: ...
    @callback
    @override
    def _async_handle_unavailable(self, service_info: bluetooth.BluetoothServiceInfoBleak) -> None: ...
    @callback
    @override
    def _async_handle_bluetooth_event(self, service_info: bluetooth.BluetoothServiceInfoBleak, change: bluetooth.BluetoothChange) -> None: ...
    @callback
    def _handle_disconnect(self) -> None: ...
    async def async_shutdown(self) -> None: ...
