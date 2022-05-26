import sqlalchemy
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime as dt
from homeassistant.components.recorder.models import EventData as EventData, Events as Events, JSONB_VARIENT_CAST as JSONB_VARIENT_CAST, JSON_VARIENT_CAST as JSON_VARIENT_CAST, StateAttributes as StateAttributes, States as States
from sqlalchemy import JSON
from sqlalchemy.orm import Query as Query
from sqlalchemy.sql.elements import ClauseList as ClauseList
from sqlalchemy.sql.selectable import Select as Select
from typing import Any

CONTINUOUS_DOMAINS: Incomplete
CONTINUOUS_ENTITY_ID_LIKE: Incomplete
UNIT_OF_MEASUREMENT_JSON: str
UNIT_OF_MEASUREMENT_JSON_LIKE: Incomplete
OLD_STATE: Incomplete

class JSONLiteral(JSON):
    def literal_processor(self, dialect: str) -> Callable[[Any], str]: ...

EVENT_DATA_JSON: Incomplete
OLD_FORMAT_EVENT_DATA_JSON: Incomplete
SHARED_ATTRS_JSON: Incomplete
OLD_FORMAT_ATTRS_JSON: Incomplete
PSUEDO_EVENT_STATE_CHANGED: Incomplete
EVENT_COLUMNS: Incomplete
STATE_COLUMNS: Incomplete
STATE_CONTEXT_ONLY_COLUMNS: Incomplete
EVENT_COLUMNS_FOR_STATE_SELECT: Incomplete
EMPTY_STATE_COLUMNS: Incomplete
EVENT_ROWS_NO_STATES: Incomplete
CONTEXT_ONLY: Incomplete
NOT_CONTEXT_ONLY: Incomplete

def select_events_context_id_subquery(start_day: dt, end_day: dt, event_types: tuple[str, ...]) -> Select: ...
def select_events_context_only() -> Select: ...
def select_states_context_only() -> Select: ...
def select_events_without_states(start_day: dt, end_day: dt, event_types: tuple[str, ...]) -> Select: ...
def select_states() -> Select: ...
def legacy_select_events_context_id(start_day: dt, end_day: dt, context_id: str) -> Select: ...
def apply_states_filters(query: Query, start_day: dt, end_day: dt) -> Query: ...
def _missing_state_matcher() -> sqlalchemy.and_: ...
def _not_continuous_entity_matcher() -> sqlalchemy.or_: ...
def _not_continuous_domain_matcher() -> sqlalchemy.and_: ...
def _continuous_domain_matcher() -> sqlalchemy.or_: ...
def _not_uom_attributes_matcher() -> ClauseList: ...
