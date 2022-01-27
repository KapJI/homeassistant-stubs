from collections.abc import Awaitable, Callable as Callable
from homeassistant.const import EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START
from homeassistant.core import Event as Event, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback

def async_at_start(hass: HomeAssistant, at_start_cb: Callable[[HomeAssistant], Union[Awaitable[None], None]]) -> None: ...
