import abc
import logging
from .api import async_address_present as async_address_present, async_last_service_info as async_last_service_info, async_register_callback as async_register_callback, async_track_unavailable as async_track_unavailable
from .match import BluetoothCallbackMatcher as BluetoothCallbackMatcher
from .models import BluetoothChange as BluetoothChange, BluetoothScanningMode as BluetoothScanningMode, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback

class BasePassiveBluetoothCoordinator(ABC, metaclass=abc.ABCMeta):
    hass: Incomplete
    logger: Incomplete
    address: Incomplete
    connectable: Incomplete
    _on_stop: Incomplete
    mode: Incomplete
    _last_unavailable_time: float
    _last_name: Incomplete
    _available: Incomplete
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, address: str, mode: BluetoothScanningMode, connectable: bool) -> None: ...
    def async_start(self) -> CALLBACK_TYPE: ...
    @abstractmethod
    def _async_handle_bluetooth_event(self, service_info: BluetoothServiceInfoBleak, change: BluetoothChange) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def last_seen(self) -> float: ...
    @property
    def available(self) -> bool: ...
    def _async_start(self) -> None: ...
    def _async_stop(self) -> None: ...
    def _async_handle_unavailable(self, service_info: BluetoothServiceInfoBleak) -> None: ...
