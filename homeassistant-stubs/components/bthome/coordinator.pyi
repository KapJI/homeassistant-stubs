from .const import CONF_SLEEPY_DEVICE as CONF_SLEEPY_DEVICE
from _typeshed import Incomplete
from bthome_ble import BTHomeBluetoothDeviceData as BTHomeBluetoothDeviceData, SensorUpdate
from collections.abc import Callable as Callable
from homeassistant.components.bluetooth import BluetoothScanningMode as BluetoothScanningMode, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothDataProcessor as PassiveBluetoothDataProcessor, PassiveBluetoothProcessorCoordinator as PassiveBluetoothProcessorCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from logging import Logger

class BTHomePassiveBluetoothProcessorCoordinator(PassiveBluetoothProcessorCoordinator[SensorUpdate]):
    discovered_event_classes: Incomplete
    device_data: Incomplete
    entry: Incomplete
    def __init__(self, hass: HomeAssistant, logger: Logger, address: str, mode: BluetoothScanningMode, update_method: Callable[[BluetoothServiceInfoBleak], SensorUpdate], device_data: BTHomeBluetoothDeviceData, discovered_event_classes: set[str], entry: ConfigEntry, connectable: bool = False) -> None: ...
    @property
    def sleepy_device(self) -> bool: ...

class BTHomePassiveBluetoothDataProcessor(PassiveBluetoothDataProcessor[_T, SensorUpdate]):
    coordinator: BTHomePassiveBluetoothProcessorCoordinator
