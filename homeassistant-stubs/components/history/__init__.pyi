from _typeshed import Incomplete
from aiohttp import web
from collections.abc import Iterable
from datetime import datetime as dt
from homeassistant.components import frontend as frontend, websocket_api as websocket_api
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.components.recorder import get_instance as get_instance, history as history
from homeassistant.components.recorder.filters import Filters as Filters, sqlalchemy_filter_from_include_exclude_conf as sqlalchemy_filter_from_include_exclude_conf
from homeassistant.components.recorder.util import session_scope as session_scope
from homeassistant.components.websocket_api import messages as messages
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entityfilter import INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA as INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA
from homeassistant.helpers.json import JSON_DUMP as JSON_DUMP
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
DOMAIN: str
HISTORY_FILTERS: str
HISTORY_USE_INCLUDE_ORDER: str
CONF_ORDER: str
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _ws_get_significant_states(hass: HomeAssistant, msg_id: int, start_time: dt, end_time: Union[dt, None], entity_ids: Union[list[str], None], filters: Union[Filters, None], use_include_order: Union[bool, None], include_start_time_state: bool, significant_changes_only: bool, minimal_response: bool, no_attributes: bool) -> str: ...
async def ws_get_history_during_period(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...

class HistoryPeriodView(HomeAssistantView):
    url: str
    name: str
    extra_urls: Incomplete
    filters: Incomplete
    use_include_order: Incomplete
    def __init__(self, filters: Union[Filters, None], use_include_order: bool) -> None: ...
    async def get(self, request: web.Request, datetime: Union[str, None] = ...) -> web.Response: ...
    def _sorted_significant_states_json(self, hass: HomeAssistant, start_time: dt, end_time: dt, entity_ids: Union[list[str], None], include_start_time_state: bool, significant_changes_only: bool, minimal_response: bool, no_attributes: bool) -> web.Response: ...

def _entities_may_have_state_changes_after(hass: HomeAssistant, entity_ids: Iterable, start_time: dt) -> bool: ...
