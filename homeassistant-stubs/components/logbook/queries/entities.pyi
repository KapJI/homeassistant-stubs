from .common import apply_events_context_hints as apply_events_context_hints, apply_states_context_hints as apply_states_context_hints, apply_states_filters as apply_states_filters, select_events_context_id_subquery as select_events_context_id_subquery, select_events_context_only as select_events_context_only, select_events_without_states as select_events_without_states, select_states as select_states, select_states_context_only as select_states_context_only
from collections.abc import Collection, Iterable
from homeassistant.components.recorder.db_schema import ENTITY_ID_IN_EVENT as ENTITY_ID_IN_EVENT, EventData as EventData, EventTypes as EventTypes, Events as Events, METADATA_ID_LAST_UPDATED_INDEX_TS as METADATA_ID_LAST_UPDATED_INDEX_TS, OLD_ENTITY_ID_IN_EVENT as OLD_ENTITY_ID_IN_EVENT, States as States, StatesMeta as StatesMeta
from sqlalchemy.sql.elements import ColumnElement as ColumnElement
from sqlalchemy.sql.lambdas import StatementLambdaElement as StatementLambdaElement
from sqlalchemy.sql.selectable import CTE as CTE, CompoundSelect as CompoundSelect, Select as Select

def _select_entities_context_ids_sub_query(start_day: float, end_day: float, event_types: tuple[str, ...], states_metadata_ids: Collection[int], json_quoted_entity_ids: list[str]) -> Select: ...
def _apply_entities_context_union(sel: Select, start_day: float, end_day: float, event_types: tuple[str, ...], states_metadata_ids: Collection[int], json_quoted_entity_ids: list[str]) -> CompoundSelect: ...
def entities_stmt(start_day: float, end_day: float, event_types: tuple[str, ...], states_metadata_ids: Collection[int], json_quoted_entity_ids: list[str]) -> StatementLambdaElement: ...
def states_select_for_entity_ids(start_day: float, end_day: float, states_metadata_ids: Collection[int]) -> Select: ...
def apply_event_entity_id_matchers(json_quoted_entity_ids: Iterable[str]) -> ColumnElement[bool]: ...
def apply_entities_hints(sel: Select) -> Select: ...
