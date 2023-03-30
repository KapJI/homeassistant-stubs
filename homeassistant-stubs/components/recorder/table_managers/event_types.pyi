from . import BaseLRUTableManager as BaseLRUTableManager
from ..const import SQLITE_MAX_BIND_VARS as SQLITE_MAX_BIND_VARS
from ..core import Recorder as Recorder
from ..db_schema import EventTypes as EventTypes
from ..queries import find_event_type_ids as find_event_type_ids
from ..util import chunked as chunked, execute_stmt_lambda_element as execute_stmt_lambda_element
from collections.abc import Iterable
from homeassistant.core import Event as Event
from sqlalchemy.orm.session import Session as Session

CACHE_SIZE: int

class EventTypeManager(BaseLRUTableManager[EventTypes]):
    def __init__(self, recorder: Recorder) -> None: ...
    def load(self, events: list[Event], session: Session) -> None: ...
    def get(self, event_type: str, session: Session) -> Union[int, None]: ...
    def get_many(self, event_types: Iterable[str], session: Session) -> dict[str, Union[int, None]]: ...
    def add_pending(self, db_event_type: EventTypes) -> None: ...
    def post_commit_pending(self) -> None: ...
    def evict_purged(self, event_types: Iterable[str]) -> None: ...
