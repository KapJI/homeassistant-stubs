from .common import apply_states_filters as apply_states_filters, select_events_without_states as select_events_without_states, select_states as select_states
from homeassistant.components.recorder.db_schema import Events as Events, LAST_UPDATED_INDEX_TS as LAST_UPDATED_INDEX_TS, States as States
from homeassistant.components.recorder.filters import Filters as Filters
from sqlalchemy.sql.lambdas import StatementLambdaElement as StatementLambdaElement
from sqlalchemy.sql.selectable import Select as Select

def all_stmt(start_day: float, end_day: float, event_type_ids: tuple[int, ...], filters: Filters | None, context_id_bin: bytes | None = None) -> StatementLambdaElement: ...
def _states_query_for_all(start_day: float, end_day: float) -> Select: ...
def _apply_all_hints(sel: Select) -> Select: ...
def _states_query_for_context_id(start_day: float, end_day: float, context_id_bin: bytes) -> Select: ...
