from .common import apply_events_context_hints as apply_events_context_hints, apply_states_context_hints as apply_states_context_hints, select_events_context_id_subquery as select_events_context_id_subquery, select_events_context_only as select_events_context_only, select_events_without_states as select_events_without_states, select_states_context_only as select_states_context_only
from collections.abc import Iterable
from homeassistant.components.recorder.db_schema import DEVICE_ID_IN_EVENT as DEVICE_ID_IN_EVENT, EventData as EventData, EventTypes as EventTypes, Events as Events, States as States, StatesMeta as StatesMeta
from sqlalchemy.sql.elements import BooleanClauseList as BooleanClauseList
from sqlalchemy.sql.lambdas import StatementLambdaElement as StatementLambdaElement
from sqlalchemy.sql.selectable import CTE as CTE, CompoundSelect as CompoundSelect, Select as Select

def _select_device_id_context_ids_sub_query(start_day: float, end_day: float, event_types: tuple[str, ...], json_quotable_device_ids: list[str]) -> Select: ...
def _apply_devices_context_union(sel: Select, start_day: float, end_day: float, event_types: tuple[str, ...], json_quotable_device_ids: list[str]) -> CompoundSelect: ...
def devices_stmt(start_day: float, end_day: float, event_types: tuple[str, ...], json_quotable_device_ids: list[str]) -> StatementLambdaElement: ...
def apply_event_device_id_matchers(json_quotable_device_ids: Iterable[str]) -> BooleanClauseList: ...
