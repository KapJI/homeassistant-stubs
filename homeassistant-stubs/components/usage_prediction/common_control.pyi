from .models import EntityUsagePredictions as EntityUsagePredictions
from _typeshed import Incomplete
from collections import Counter
from functools import cache
from homeassistant.components.recorder import get_instance as get_instance
from homeassistant.components.recorder.db_schema import EventData as EventData, EventTypes as EventTypes, Events as Events
from homeassistant.components.recorder.models import uuid_hex_to_bytes_or_none as uuid_hex_to_bytes_or_none
from homeassistant.components.recorder.util import session_scope as session_scope
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.util.json import json_loads_object as json_loads_object
from typing import Literal

_LOGGER: Incomplete
TIME_CATEGORIES: Incomplete
RESULTS_TO_INCLUDE: int
QUERY_YIELD_PER: int
ALLOWED_DOMAINS: Incomplete

@cache
def time_category(hour: int) -> Literal['morning', 'afternoon', 'evening', 'night']: ...
async def async_predict_common_control(hass: HomeAssistant, user_id: str) -> EntityUsagePredictions: ...
def _fetch_and_process_data(hass: HomeAssistant, user_id: str, allowed_entities: set[str]) -> dict[str, Counter[str]]: ...
