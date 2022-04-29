from .models import LazyState as LazyState, RecorderRuns as RecorderRuns, StateAttributes as StateAttributes, States as States, process_timestamp as process_timestamp, process_timestamp_to_utc_isoformat as process_timestamp_to_utc_isoformat
from .util import execute as execute, session_scope as session_scope
from _typeshed import Incomplete
from collections.abc import Iterable, MutableMapping
from datetime import datetime
from homeassistant.components import recorder as recorder
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, split_entity_id as split_entity_id
from sqlalchemy import Column as Column
from sqlalchemy.orm.session import Session as Session
from typing import Any

_LOGGER: Incomplete
STATE_KEY: str
LAST_CHANGED_KEY: str
SIGNIFICANT_DOMAINS: Incomplete
SIGNIFICANT_DOMAINS_ENTITY_ID_LIKE: Incomplete
IGNORE_DOMAINS: Incomplete
IGNORE_DOMAINS_ENTITY_ID_LIKE: Incomplete
NEED_ATTRIBUTE_DOMAINS: Incomplete
BASE_STATES: Incomplete
BASE_STATES_NO_LAST_UPDATED: Incomplete
QUERY_STATE_NO_ATTR: Incomplete
QUERY_STATE_NO_ATTR_NO_LAST_UPDATED: Incomplete
QUERY_STATES_PRE_SCHEMA_25: Incomplete
QUERY_STATES_PRE_SCHEMA_25_NO_LAST_UPDATED: Incomplete
QUERY_STATES: Incomplete
QUERY_STATES_NO_LAST_UPDATED: Incomplete
HISTORY_BAKERY: str

def query_and_join_attributes(hass: HomeAssistant, no_attributes: bool) -> tuple[list[Column], bool]: ...
def bake_query_and_join_attributes(hass: HomeAssistant, no_attributes: bool, include_last_updated: bool = ...) -> tuple[Any, bool]: ...
def async_setup(hass: HomeAssistant) -> None: ...
def get_significant_states(hass: HomeAssistant, start_time: datetime, end_time: Union[datetime, None] = ..., entity_ids: Union[list[str], None] = ..., filters: Union[Any, None] = ..., include_start_time_state: bool = ..., significant_changes_only: bool = ..., minimal_response: bool = ..., no_attributes: bool = ...) -> MutableMapping[str, list[Union[State, dict[str, Any]]]]: ...
def _query_significant_states_with_session(hass: HomeAssistant, session: Session, start_time: datetime, end_time: Union[datetime, None] = ..., entity_ids: Union[list[str], None] = ..., filters: Any = ..., significant_changes_only: bool = ..., no_attributes: bool = ...) -> list[States]: ...
def get_significant_states_with_session(hass: HomeAssistant, session: Session, start_time: datetime, end_time: Union[datetime, None] = ..., entity_ids: Union[list[str], None] = ..., filters: Any = ..., include_start_time_state: bool = ..., significant_changes_only: bool = ..., minimal_response: bool = ..., no_attributes: bool = ...) -> MutableMapping[str, list[Union[State, dict[str, Any]]]]: ...
def get_full_significant_states_with_session(hass: HomeAssistant, session: Session, start_time: datetime, end_time: Union[datetime, None] = ..., entity_ids: Union[list[str], None] = ..., filters: Any = ..., include_start_time_state: bool = ..., significant_changes_only: bool = ..., no_attributes: bool = ...) -> MutableMapping[str, list[State]]: ...
def state_changes_during_period(hass: HomeAssistant, start_time: datetime, end_time: Union[datetime, None] = ..., entity_id: Union[str, None] = ..., no_attributes: bool = ..., descending: bool = ..., limit: Union[int, None] = ..., include_start_time_state: bool = ...) -> MutableMapping[str, list[State]]: ...
def get_last_state_changes(hass: HomeAssistant, number_of_states: int, entity_id: str) -> MutableMapping[str, list[State]]: ...
def _get_states_with_session(hass: HomeAssistant, session: Session, utc_point_in_time: datetime, entity_ids: Union[list[str], None] = ..., run: Union[RecorderRuns, None] = ..., filters: Union[Any, None] = ..., no_attributes: bool = ...) -> list[State]: ...
def _get_single_entity_states_with_session(hass: HomeAssistant, session: Session, utc_point_in_time: datetime, entity_id: str, no_attributes: bool = ...) -> list[State]: ...
def _sorted_states_to_dict(hass: HomeAssistant, session: Session, states: Iterable[States], start_time: datetime, entity_ids: Union[list[str], None], filters: Any = ..., include_start_time_state: bool = ..., minimal_response: bool = ..., no_attributes: bool = ...) -> MutableMapping[str, list[Union[State, dict[str, Any]]]]: ...
