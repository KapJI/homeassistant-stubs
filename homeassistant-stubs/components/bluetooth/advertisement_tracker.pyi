from .models import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from typing import Any

ADVERTISING_TIMES_NEEDED: int
TRACKER_BUFFERING_WOBBLE_SECONDS: int

class AdvertisementTracker:
    __slots__: Incomplete
    intervals: Incomplete
    fallback_intervals: Incomplete
    sources: Incomplete
    _timings: Incomplete
    def __init__(self) -> None: ...
    def async_diagnostics(self) -> dict[str, dict[str, Any]]: ...
    def async_collect(self, service_info: BluetoothServiceInfoBleak) -> None: ...
    def async_remove_address(self, address: str) -> None: ...
    def async_remove_fallback_interval(self, address: str) -> None: ...
    def async_remove_source(self, source: str) -> None: ...
