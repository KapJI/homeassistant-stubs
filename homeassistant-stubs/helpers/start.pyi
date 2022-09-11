from collections.abc import Callable as Callable, Coroutine
from homeassistant.const import EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from typing import Any

def async_at_start(hass: HomeAssistant, at_start_cb: Callable[[HomeAssistant], Union[Coroutine[Any, Any, None], None]]) -> CALLBACK_TYPE: ...
