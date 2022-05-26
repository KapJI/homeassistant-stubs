from .helpers import async_determine_event_types as async_determine_event_types
from .processor import EventProcessor as EventProcessor
from _typeshed import Incomplete
from aiohttp import web
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.components.recorder import get_instance as get_instance
from homeassistant.components.recorder.filters import Filters as Filters
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import InvalidEntityFormatError as InvalidEntityFormatError
from homeassistant.helpers.entityfilter import EntityFilter as EntityFilter
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

def async_setup(hass: HomeAssistant, conf: ConfigType, filters: Union[Filters, None], entities_filter: Union[EntityFilter, None]) -> None: ...

class LogbookView(HomeAssistantView):
    url: str
    name: str
    extra_urls: Incomplete
    config: Incomplete
    filters: Incomplete
    entities_filter: Incomplete
    def __init__(self, config: dict[str, Any], filters: Union[Filters, None], entities_filter: Union[EntityFilter, None]) -> None: ...
    async def get(self, request: web.Request, datetime: Union[str, None] = ...) -> web.Response: ...
