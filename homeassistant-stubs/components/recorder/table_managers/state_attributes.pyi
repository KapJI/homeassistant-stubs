from . import BaseLRUTableManager as BaseLRUTableManager
from ..core import Recorder as Recorder
from ..db_schema import StateAttributes as StateAttributes
from ..queries import get_shared_attributes as get_shared_attributes
from ..util import execute_stmt_lambda_element as execute_stmt_lambda_element
from _typeshed import Incomplete
from collections.abc import Collection, Iterable
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData
from homeassistant.util.collection import chunked_or_all as chunked_or_all
from homeassistant.util.json import JSON_ENCODE_EXCEPTIONS as JSON_ENCODE_EXCEPTIONS
from sqlalchemy.orm.session import Session as Session

CACHE_SIZE: int
_LOGGER: Incomplete

class StateAttributesManager(BaseLRUTableManager[StateAttributes]):
    def __init__(self, recorder: Recorder) -> None: ...
    def serialize_from_event(self, event: Event[EventStateChangedData]) -> bytes | None: ...
    def load(self, events: list[Event[EventStateChangedData]], session: Session) -> None: ...
    def get(self, shared_attr: str, data_hash: int, session: Session) -> int | None: ...
    def get_many(self, shared_attrs_data_hashes: Iterable[tuple[str, int]], session: Session) -> dict[str, int | None]: ...
    def _load_from_hashes(self, hashes: Collection[int], session: Session) -> dict[str, int | None]: ...
    def add_pending(self, db_state_attributes: StateAttributes) -> None: ...
    def post_commit_pending(self) -> None: ...
    def evict_purged(self, attributes_ids: set[int]) -> None: ...
