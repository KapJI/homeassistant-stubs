from ..filters import Filters
from .const import NEED_ATTRIBUTE_DOMAINS as NEED_ATTRIBUTE_DOMAINS, SIGNIFICANT_DOMAINS as SIGNIFICANT_DOMAINS
from collections.abc import MutableMapping
from datetime import datetime
from homeassistant.core import HomeAssistant, State
from sqlalchemy.orm.session import Session
from typing import Any

__all__ = ['NEED_ATTRIBUTE_DOMAINS', 'SIGNIFICANT_DOMAINS', 'get_full_significant_states_with_session', 'get_last_state_changes', 'get_significant_states', 'get_significant_states_with_session', 'state_changes_during_period']

def get_full_significant_states_with_session(hass: HomeAssistant, session: Session, start_time: datetime, end_time: datetime | None = None, entity_ids: list[str] | None = None, filters: Filters | None = None, include_start_time_state: bool = True, significant_changes_only: bool = True, no_attributes: bool = False) -> MutableMapping[str, list[State]]: ...
def get_last_state_changes(hass: HomeAssistant, number_of_states: int, entity_id: str) -> MutableMapping[str, list[State]]: ...
def get_significant_states(hass: HomeAssistant, start_time: datetime, end_time: datetime | None = None, entity_ids: list[str] | None = None, filters: Filters | None = None, include_start_time_state: bool = True, significant_changes_only: bool = True, minimal_response: bool = False, no_attributes: bool = False, compressed_state_format: bool = False) -> MutableMapping[str, list[State | dict[str, Any]]]: ...
def get_significant_states_with_session(hass: HomeAssistant, session: Session, start_time: datetime, end_time: datetime | None = None, entity_ids: list[str] | None = None, filters: Filters | None = None, include_start_time_state: bool = True, significant_changes_only: bool = True, minimal_response: bool = False, no_attributes: bool = False, compressed_state_format: bool = False) -> MutableMapping[str, list[State | dict[str, Any]]]: ...
def state_changes_during_period(hass: HomeAssistant, start_time: datetime, end_time: datetime | None = None, entity_id: str | None = None, no_attributes: bool = False, descending: bool = False, limit: int | None = None, include_start_time_state: bool = True) -> MutableMapping[str, list[State]]: ...
