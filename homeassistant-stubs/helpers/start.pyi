from collections.abc import Awaitable
from homeassistant.const import EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from typing import Callable

def async_at_start(hass: HomeAssistant, at_start_cb: Callable[[HomeAssistant], Awaitable]) -> None: ...
