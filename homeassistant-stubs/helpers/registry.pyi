import abc
from .storage import Store as Store
from abc import ABC, abstractmethod
from homeassistant.core import CoreState as CoreState, HomeAssistant as HomeAssistant, callback as callback
from typing import Any

SAVE_DELAY: int
SAVE_DELAY_LONG: int

class BaseRegistry(ABC, metaclass=abc.ABCMeta):
    hass: HomeAssistant
    _store: Store
    def async_schedule_save(self) -> None: ...
    @abstractmethod
    def _data_to_save(self) -> dict[str, Any]: ...
