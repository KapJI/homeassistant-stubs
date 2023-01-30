import sqlalchemy
from .common import apply_events_context_hints as apply_events_context_hints, apply_states_context_hints as apply_states_context_hints, select_events_context_id_subquery as select_events_context_id_subquery, select_events_context_only as select_events_context_only, select_events_without_states as select_events_without_states, select_states_context_only as select_states_context_only
from .devices import apply_event_device_id_matchers as apply_event_device_id_matchers
from .entities import apply_entities_hints as apply_entities_hints, apply_event_entity_id_matchers as apply_event_entity_id_matchers, states_query_for_entity_ids as states_query_for_entity_ids
from collections.abc import Iterable
from homeassistant.components.recorder.db_schema import EventData as EventData, Events as Events, States as States
from sqlalchemy.orm import Query as Query
from sqlalchemy.sql.lambdas import StatementLambdaElement as StatementLambdaElement
from sqlalchemy.sql.selectable import CTE as CTE, CompoundSelect as CompoundSelect

def _select_entities_device_id_context_ids_sub_query(start_day: float, end_day: float, event_types: tuple[str, ...], entity_ids: list[str], json_quoted_entity_ids: list[str], json_quoted_device_ids: list[str]) -> CompoundSelect: ...
def _apply_entities_devices_context_union(query: Query, start_day: float, end_day: float, event_types: tuple[str, ...], entity_ids: list[str], json_quoted_entity_ids: list[str], json_quoted_device_ids: list[str]) -> CompoundSelect: ...
def entities_devices_stmt(start_day: float, end_day: float, event_types: tuple[str, ...], entity_ids: list[str], json_quoted_entity_ids: list[str], json_quoted_device_ids: list[str]) -> StatementLambdaElement: ...
def _apply_event_entity_id_device_id_matchers(json_quoted_entity_ids: Iterable[str], json_quoted_device_ids: Iterable[str]) -> sqlalchemy.or_: ...
