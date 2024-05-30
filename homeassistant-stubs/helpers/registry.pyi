import abc
from .storage import Store as Store
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections import UserDict
from collections.abc import Mapping as Mapping, Sequence as Sequence, ValuesView
from homeassistant.core import CoreState as CoreState, HomeAssistant as HomeAssistant, callback as callback

SAVE_DELAY: int
SAVE_DELAY_LONG: int
RegistryIndexType: Incomplete

class BaseRegistryItems(UserDict[str, _DataT], ABC, metaclass=abc.ABCMeta):
    data: dict[str, _DataT]
    def values(self) -> ValuesView[_DataT]: ...
    @abstractmethod
    def _index_entry(self, key: str, entry: _DataT) -> None: ...
    @abstractmethod
    def _unindex_entry(self, key: str, replacement_entry: _DataT | None = None) -> None: ...
    def __setitem__(self, key: str, entry: _DataT) -> None: ...
    def _unindex_entry_value(self, key: str, value: str, index: RegistryIndexType) -> None: ...
    def __delitem__(self, key: str) -> None: ...

class BaseRegistry(ABC, metaclass=abc.ABCMeta):
    hass: HomeAssistant
    _store: Store[_StoreDataT]
    def async_schedule_save(self) -> None: ...
    @abstractmethod
    def _data_to_save(self) -> _StoreDataT: ...
