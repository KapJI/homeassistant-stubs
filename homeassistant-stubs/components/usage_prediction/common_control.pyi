from .models import EntityUsagePredictions as EntityUsagePredictions
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Sequence
from functools import cache
from homeassistant.components.recorder import get_instance as get_instance
from homeassistant.components.recorder.db_schema import EventData as EventData, EventTypes as EventTypes, Events as Events
from homeassistant.components.recorder.models import uuid_hex_to_bytes_or_none as uuid_hex_to_bytes_or_none
from homeassistant.components.recorder.util import session_scope as session_scope
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_registry as er
from homeassistant.util.json import json_loads_object as json_loads_object
from sqlalchemy.engine.row import Row as Row
from sqlalchemy.orm import Session as Session
from typing import Literal

_LOGGER: Incomplete
TIME_CATEGORIES: Incomplete
RESULTS_TO_INCLUDE: int
ALLOWED_DOMAINS: Incomplete

@cache
def time_category(hour: int) -> Literal['morning', 'afternoon', 'evening', 'night']: ...
async def async_predict_common_control(hass: HomeAssistant, user_id: str) -> EntityUsagePredictions: ...
def _fetch_and_process_data(session: Session, ent_reg: er.EntityRegistry, user_id: str) -> Sequence[Row[tuple[bytes | None, float | None, str | None]]]: ...
def _fetch_with_session(hass: HomeAssistant, fetch_func: Callable[[Session], Sequence[Row[tuple[bytes | None, float | None, str | None]]]], *args: object) -> Sequence[Row[tuple[bytes | None, float | None, str | None]]]: ...
