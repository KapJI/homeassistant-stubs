from ... import recorder as recorder
from ..db_schema import RecorderRuns as RecorderRuns, StateAttributes as StateAttributes, States as States
from ..filters import Filters as Filters
from ..models import process_datetime_to_timestamp as process_datetime_to_timestamp, process_timestamp as process_timestamp, process_timestamp_to_utc_isoformat as process_timestamp_to_utc_isoformat
from ..models.legacy import LegacyLazyState as LegacyLazyState, LegacyLazyStatePreSchema31 as LegacyLazyStatePreSchema31, legacy_row_to_compressed_state as legacy_row_to_compressed_state, legacy_row_to_compressed_state_pre_schema_31 as legacy_row_to_compressed_state_pre_schema_31
from ..util import execute_stmt_lambda_element as execute_stmt_lambda_element, session_scope as session_scope
from .common import _schema_version as _schema_version
from .const import LAST_CHANGED_KEY as LAST_CHANGED_KEY, NEED_ATTRIBUTE_DOMAINS as NEED_ATTRIBUTE_DOMAINS, SIGNIFICANT_DOMAINS as SIGNIFICANT_DOMAINS, SIGNIFICANT_DOMAINS_ENTITY_ID_LIKE as SIGNIFICANT_DOMAINS_ENTITY_ID_LIKE, STATE_KEY as STATE_KEY
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable, MutableMapping
from datetime import datetime
from homeassistant.const import COMPRESSED_STATE_LAST_UPDATED as COMPRESSED_STATE_LAST_UPDATED, COMPRESSED_STATE_STATE as COMPRESSED_STATE_STATE
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, split_entity_id as split_entity_id
from sqlalchemy import Column as Column
from sqlalchemy.engine.row import Row as Row
from sqlalchemy.orm.session import Session as Session
from sqlalchemy.sql.lambdas import StatementLambdaElement as StatementLambdaElement
from typing import Any

_BASE_STATES: Incomplete
_BASE_STATES_NO_LAST_CHANGED: Incomplete
_QUERY_STATE_NO_ATTR: Incomplete
_QUERY_STATE_NO_ATTR_NO_LAST_CHANGED: Incomplete
_BASE_STATES_PRE_SCHEMA_31: Incomplete
_BASE_STATES_NO_LAST_CHANGED_PRE_SCHEMA_31: Incomplete
_QUERY_STATE_NO_ATTR_PRE_SCHEMA_31: Incomplete
_QUERY_STATE_NO_ATTR_NO_LAST_CHANGED_PRE_SCHEMA_31: Incomplete
_QUERY_STATES_PRE_SCHEMA_25: Incomplete
_QUERY_STATES_PRE_SCHEMA_25_NO_LAST_CHANGED: Incomplete
_QUERY_STATES_PRE_SCHEMA_31: Incomplete
_QUERY_STATES_NO_LAST_CHANGED_PRE_SCHEMA_31: Incomplete
_QUERY_STATES: Incomplete
_QUERY_STATES_NO_LAST_CHANGED: Incomplete
_FIELD_MAP: Incomplete
_FIELD_MAP_PRE_SCHEMA_31: Incomplete

def _lambda_stmt_and_join_attributes(schema_version: int, no_attributes: bool, include_last_changed: bool = ...) -> tuple[StatementLambdaElement, bool]: ...
def get_significant_states(hass: HomeAssistant, start_time: datetime, end_time: datetime | None = ..., entity_ids: list[str] | None = ..., filters: Filters | None = ..., include_start_time_state: bool = ..., significant_changes_only: bool = ..., minimal_response: bool = ..., no_attributes: bool = ..., compressed_state_format: bool = ...) -> MutableMapping[str, list[State | dict[str, Any]]]: ...
def _significant_states_stmt(schema_version: int, start_time: datetime, end_time: datetime | None, entity_ids: list[str], significant_changes_only: bool, no_attributes: bool) -> StatementLambdaElement: ...
def get_significant_states_with_session(hass: HomeAssistant, session: Session, start_time: datetime, end_time: datetime | None = ..., entity_ids: list[str] | None = ..., filters: Filters | None = ..., include_start_time_state: bool = ..., significant_changes_only: bool = ..., minimal_response: bool = ..., no_attributes: bool = ..., compressed_state_format: bool = ...) -> MutableMapping[str, list[State | dict[str, Any]]]: ...
def get_full_significant_states_with_session(hass: HomeAssistant, session: Session, start_time: datetime, end_time: datetime | None = ..., entity_ids: list[str] | None = ..., filters: Filters | None = ..., include_start_time_state: bool = ..., significant_changes_only: bool = ..., no_attributes: bool = ...) -> MutableMapping[str, list[State]]: ...
def _state_changed_during_period_stmt(schema_version: int, start_time: datetime, end_time: datetime | None, entity_id: str, no_attributes: bool, descending: bool, limit: int | None) -> StatementLambdaElement: ...
def state_changes_during_period(hass: HomeAssistant, start_time: datetime, end_time: datetime | None = ..., entity_id: str | None = ..., no_attributes: bool = ..., descending: bool = ..., limit: int | None = ..., include_start_time_state: bool = ...) -> MutableMapping[str, list[State]]: ...
def _get_last_state_changes_stmt(schema_version: int, number_of_states: int, entity_id: str) -> StatementLambdaElement: ...
def get_last_state_changes(hass: HomeAssistant, number_of_states: int, entity_id: str) -> MutableMapping[str, list[State]]: ...
def _get_states_for_entities_stmt(schema_version: int, run_start: datetime, utc_point_in_time: datetime, entity_ids: list[str], no_attributes: bool) -> StatementLambdaElement: ...
def _get_rows_with_session(hass: HomeAssistant, session: Session, utc_point_in_time: datetime, entity_ids: list[str], run: RecorderRuns | None = ..., no_attributes: bool = ...) -> Iterable[Row]: ...
def _get_single_entity_states_stmt(schema_version: int, utc_point_in_time: datetime, entity_id: str, no_attributes: bool = ...) -> StatementLambdaElement: ...
def _sorted_states_to_dict(hass: HomeAssistant, session: Session, states: Iterable[Row], start_time: datetime, entity_ids: list[str], include_start_time_state: bool = ..., minimal_response: bool = ..., no_attributes: bool = ..., compressed_state_format: bool = ...) -> MutableMapping[str, list[State | dict[str, Any]]]: ...
