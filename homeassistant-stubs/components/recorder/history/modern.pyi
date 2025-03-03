from ..const import LAST_REPORTED_SCHEMA_VERSION as LAST_REPORTED_SCHEMA_VERSION, MAX_IDS_FOR_INDEXED_GROUP_BY as MAX_IDS_FOR_INDEXED_GROUP_BY
from ..db_schema import SHARED_ATTR_OR_LEGACY_ATTRIBUTES as SHARED_ATTR_OR_LEGACY_ATTRIBUTES, StateAttributes as StateAttributes, States as States, StatesMeta as StatesMeta
from ..filters import Filters as Filters
from ..models import LazyState as LazyState, datetime_to_timestamp_or_none as datetime_to_timestamp_or_none, extract_metadata_ids as extract_metadata_ids, row_to_compressed_state as row_to_compressed_state
from ..util import execute_stmt_lambda_element as execute_stmt_lambda_element, session_scope as session_scope
from .const import LAST_CHANGED_KEY as LAST_CHANGED_KEY, NEED_ATTRIBUTE_DOMAINS as NEED_ATTRIBUTE_DOMAINS, SIGNIFICANT_DOMAINS as SIGNIFICANT_DOMAINS, STATE_KEY as STATE_KEY
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from datetime import datetime
from homeassistant.const import COMPRESSED_STATE_LAST_UPDATED as COMPRESSED_STATE_LAST_UPDATED, COMPRESSED_STATE_STATE as COMPRESSED_STATE_STATE
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, split_entity_id as split_entity_id
from homeassistant.helpers.recorder import get_instance as get_instance
from homeassistant.util.collection import chunked_or_all as chunked_or_all
from sqlalchemy import CompoundSelect as CompoundSelect, Select as Select, StatementLambdaElement as StatementLambdaElement, Subquery as Subquery
from sqlalchemy.engine.row import Row
from sqlalchemy.orm.session import Session as Session
from typing import Any

_FIELD_MAP: Incomplete

def _stmt_and_join_attributes(no_attributes: bool, include_last_changed: bool, include_last_reported: bool) -> Select: ...
def _stmt_and_join_attributes_for_start_state(no_attributes: bool, include_last_changed: bool, include_last_reported: bool) -> Select: ...
def _select_from_subquery(subquery: Subquery | CompoundSelect, no_attributes: bool, include_last_changed: bool, include_last_reported: bool) -> Select: ...
def get_significant_states(hass: HomeAssistant, start_time: datetime, end_time: datetime | None = None, entity_ids: list[str] | None = None, filters: Filters | None = None, include_start_time_state: bool = True, significant_changes_only: bool = True, minimal_response: bool = False, no_attributes: bool = False, compressed_state_format: bool = False) -> dict[str, list[State | dict[str, Any]]]: ...
def _significant_states_stmt(start_time_ts: float, end_time_ts: float | None, single_metadata_id: int | None, metadata_ids: list[int], metadata_ids_in_significant_domains: list[int], significant_changes_only: bool, no_attributes: bool, include_start_time_state: bool, run_start_ts: float | None, slow_dependent_subquery: bool) -> Select | CompoundSelect: ...
def get_significant_states_with_session(hass: HomeAssistant, session: Session, start_time: datetime, end_time: datetime | None = None, entity_ids: list[str] | None = None, filters: Filters | None = None, include_start_time_state: bool = True, significant_changes_only: bool = True, minimal_response: bool = False, no_attributes: bool = False, compressed_state_format: bool = False) -> dict[str, list[State | dict[str, Any]]]: ...
def _generate_significant_states_with_session_stmt(start_time_ts: float, end_time_ts: float | None, single_metadata_id: int | None, metadata_ids: list[int], metadata_ids_in_significant_domains: list[int], significant_changes_only: bool, no_attributes: bool, include_start_time_state: bool, oldest_ts: float | None, slow_dependent_subquery: bool) -> StatementLambdaElement: ...
def get_full_significant_states_with_session(hass: HomeAssistant, session: Session, start_time: datetime, end_time: datetime | None = None, entity_ids: list[str] | None = None, filters: Filters | None = None, include_start_time_state: bool = True, significant_changes_only: bool = True, no_attributes: bool = False) -> dict[str, list[State]]: ...
def _state_changed_during_period_stmt(start_time_ts: float, end_time_ts: float | None, single_metadata_id: int, no_attributes: bool, limit: int | None, include_start_time_state: bool, run_start_ts: float | None, include_last_reported: bool) -> Select | CompoundSelect: ...
def state_changes_during_period(hass: HomeAssistant, start_time: datetime, end_time: datetime | None = None, entity_id: str | None = None, no_attributes: bool = False, descending: bool = False, limit: int | None = None, include_start_time_state: bool = True) -> dict[str, list[State]]: ...
def _get_last_state_changes_single_stmt(metadata_id: int) -> Select: ...
def _get_last_state_changes_multiple_stmt(number_of_states: int, metadata_id: int, include_last_reported: bool) -> Select: ...
def get_last_state_changes(hass: HomeAssistant, number_of_states: int, entity_id: str) -> dict[str, list[State]]: ...
def _get_start_time_state_for_entities_stmt_dependent_sub_query(epoch_time: float, metadata_ids: list[int], no_attributes: bool, include_last_changed: bool) -> Select: ...
def _get_start_time_state_for_entities_stmt_group_by(epoch_time: float, metadata_ids: list[int], no_attributes: bool, include_last_changed: bool) -> Select: ...
def _get_oldest_possible_ts(hass: HomeAssistant, utc_point_in_time: datetime) -> float | None: ...
def _get_start_time_state_stmt(epoch_time: float, single_metadata_id: int | None, metadata_ids: list[int], no_attributes: bool, include_last_changed: bool, slow_dependent_subquery: bool) -> Select: ...
def _get_single_entity_start_time_stmt(epoch_time: float, metadata_id: int, no_attributes: bool, include_last_changed: bool, include_last_reported: bool) -> Select: ...
def _sorted_states_to_dict(states: Iterable[Row], start_time_ts: float | None, entity_ids: list[str], entity_id_to_metadata_id: dict[str, int | None], minimal_response: bool = False, compressed_state_format: bool = False, descending: bool = False, no_attributes: bool = False) -> dict[str, list[State | dict[str, Any]]]: ...
