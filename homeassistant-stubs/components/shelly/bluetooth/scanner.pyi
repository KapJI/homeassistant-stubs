from _typeshed import Incomplete
from homeassistant.components.bluetooth import BaseHaRemoteScanner as BaseHaRemoteScanner
from homeassistant.core import callback as callback
from typing import Any

_LOGGER: Incomplete

class ShellyBLEScanner(BaseHaRemoteScanner):
    def async_on_event(self, event: dict[str, Any]) -> None: ...
