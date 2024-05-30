from ..core import Recorder as Recorder
from _typeshed import Incomplete
from homeassistant.util.event_type import EventType as EventType
from lru import LRU
from typing import Any

class BaseTableManager:
    _id_map: LRU[EventType[Any] | str, int]
    active: bool
    recorder: Incomplete
    _pending: Incomplete
    def __init__(self, recorder: Recorder) -> None: ...
    def get_from_cache(self, data: str) -> int | None: ...
    def get_pending(self, shared_data: EventType[Any] | str) -> _DataT | None: ...
    def reset(self) -> None: ...

class BaseLRUTableManager(BaseTableManager[_DataT]):
    _id_map: Incomplete
    def __init__(self, recorder: Recorder, lru_size: int) -> None: ...
    def adjust_lru_size(self, new_size: int) -> None: ...
