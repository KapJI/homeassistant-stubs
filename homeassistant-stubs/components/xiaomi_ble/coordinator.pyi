from .const import CONF_SLEEPY_DEVICE as CONF_SLEEPY_DEVICE
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.bluetooth import BluetoothScanningMode as BluetoothScanningMode, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from homeassistant.components.bluetooth.active_update_processor import ActiveBluetoothProcessorCoordinator as ActiveBluetoothProcessorCoordinator
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothDataProcessor as PassiveBluetoothDataProcessor
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.debounce import Debouncer as Debouncer
from logging import Logger
from typing import Any
from xiaomi_ble import XiaomiBluetoothDeviceData as XiaomiBluetoothDeviceData

class XiaomiActiveBluetoothProcessorCoordinator(ActiveBluetoothProcessorCoordinator):
    discovered_event_classes: Incomplete
    device_data: Incomplete
    entry: Incomplete
    def __init__(self, hass: HomeAssistant, logger: Logger, *, address: str, mode: BluetoothScanningMode, update_method: Callable[[BluetoothServiceInfoBleak], Any], needs_poll_method: Callable[[BluetoothServiceInfoBleak, float | None], bool], device_data: XiaomiBluetoothDeviceData, discovered_event_classes: set[str], poll_method: Callable[[BluetoothServiceInfoBleak], Coroutine[Any, Any, Any]] | None = None, poll_debouncer: Debouncer[Coroutine[Any, Any, None]] | None = None, entry: ConfigEntry, connectable: bool = True) -> None: ...
    @property
    def sleepy_device(self) -> bool: ...

class XiaomiPassiveBluetoothDataProcessor(PassiveBluetoothDataProcessor):
    coordinator: XiaomiActiveBluetoothProcessorCoordinator
