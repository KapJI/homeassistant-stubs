import abc
from .storage import Store as Store
from abc import ABC, abstractmethod
from collections import UserDict
from collections.abc import Mapping, Sequence, ValuesView
from homeassistant.core import CoreState as CoreState, HomeAssistant as HomeAssistant, callback as callback
from typing import Any, Generic, Literal, TypeVar

SAVE_DELAY: int
SAVE_DELAY_LONG: int
_DataT = TypeVar('_DataT')
_StoreDataT = TypeVar('_StoreDataT', bound=Mapping[str, Any] | Sequence[Any])

class BaseRegistryItems(UserDict[str, _DataT], ABC, metaclass=abc.ABCMeta):
    data: dict[str, _DataT]
    def values(self) -> ValuesView[_DataT]: ...
    @abstractmethod
    def _index_entry(self, key: str, entry: _DataT) -> None: ...
    @abstractmethod
    def _unindex_entry(self, key: str, replacement_entry: _DataT | None = None) -> None: ...
    def __setitem__(self, key: str, entry: _DataT) -> None: ...
    def _unindex_entry_value(self, key: str, value: str, index: dict[str, dict[str, Literal[True]]]) -> None: ...
    def __delitem__(self, key: str) -> None: ...

class BaseRegistry(ABC, Generic[_StoreDataT], metaclass=abc.ABCMeta):
    hass: HomeAssistant
    _store: Store[_StoreDataT]
    def async_schedule_save(self) -> None: ...
    @abstractmethod
    def _data_to_save(self) -> _StoreDataT: ...
