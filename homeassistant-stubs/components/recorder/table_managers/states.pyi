from ..db_schema import States as States
from ..queries import find_oldest_state as find_oldest_state
from ..util import execute_stmt_lambda_element as execute_stmt_lambda_element
from sqlalchemy.orm.session import Session as Session

class StatesManager:
    _pending: dict[str, States]
    _last_committed_id: dict[str, int]
    _last_reported: dict[int, float]
    _oldest_ts: float | None
    def __init__(self) -> None: ...
    @property
    def oldest_ts(self) -> float | None: ...
    def pop_pending(self, entity_id: str) -> States | None: ...
    def pop_committed(self, entity_id: str) -> int | None: ...
    def add_pending(self, entity_id: str, state: States) -> None: ...
    def update_pending_last_reported(self, state_id: int, last_reported_timestamp: float) -> None: ...
    def get_pending_last_reported_timestamp(self) -> dict[int, float]: ...
    def post_commit_pending(self) -> None: ...
    def reset(self) -> None: ...
    def load_from_db(self, session: Session) -> None: ...
    def evict_purged_state_ids(self, purged_state_ids: set[int]) -> None: ...
    def evict_purged_entity_ids(self, purged_entity_ids: set[str]) -> None: ...
