from ..core import Recorder as Recorder
from _typeshed import Incomplete
from typing import Generic, TypeVar

_DataT = TypeVar('_DataT')

class BaseTableManager(Generic[_DataT]):
    active: bool
    recorder: Incomplete
    _pending: Incomplete
    _id_map: Incomplete
    def __init__(self, recorder: Recorder) -> None: ...
    def get_from_cache(self, data: str) -> int | None: ...
    def get_pending(self, shared_data: str) -> _DataT | None: ...
    def reset(self) -> None: ...

class BaseLRUTableManager(BaseTableManager[_DataT]):
    _id_map: Incomplete
    def __init__(self, recorder: Recorder, lru_size: int) -> None: ...
    def adjust_lru_size(self, new_size: int) -> None: ...
