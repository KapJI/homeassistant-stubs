from . import websocket_api as websocket_api
from .const import DOMAIN as DOMAIN
from .helpers import entities_may_have_state_changes_after as entities_may_have_state_changes_after
from .models import HistoryConfig as HistoryConfig
from _typeshed import Incomplete
from aiohttp import web
from datetime import datetime as dt
from homeassistant.components import frontend as frontend
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.components.recorder import get_instance as get_instance, history as history
from homeassistant.components.recorder.filters import Filters as Filters, extract_include_exclude_filter_conf as extract_include_exclude_filter_conf, merge_include_exclude_filters as merge_include_exclude_filters, sqlalchemy_filter_from_include_exclude_conf as sqlalchemy_filter_from_include_exclude_conf
from homeassistant.components.recorder.util import session_scope as session_scope
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entityfilter import INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA as INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA, convert_include_exclude_filter as convert_include_exclude_filter
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONF_ORDER: str
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class HistoryPeriodView(HomeAssistantView):
    url: str
    name: str
    extra_urls: Incomplete
    filters: Incomplete
    def __init__(self, filters: Union[Filters, None]) -> None: ...
    async def get(self, request: web.Request, datetime: Union[str, None] = ...) -> web.Response: ...
    def _sorted_significant_states_json(self, hass: HomeAssistant, start_time: dt, end_time: dt, entity_ids: Union[list[str], None], include_start_time_state: bool, significant_changes_only: bool, minimal_response: bool, no_attributes: bool) -> web.Response: ...
