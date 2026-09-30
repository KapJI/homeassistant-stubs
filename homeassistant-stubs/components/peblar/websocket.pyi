from .const import EVENT_STREAM_RETRY_MAXIMUM as EVENT_STREAM_RETRY_MAXIMUM, EVENT_STREAM_RETRY_MINIMUM as EVENT_STREAM_RETRY_MINIMUM, LOGGER as LOGGER
from .coordinator import PeblarConfigEntry as PeblarConfigEntry
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from peblar import Peblar as Peblar, PeblarSessionStatus as PeblarSessionStatus, SessionState as SessionState

class PeblarSessionListener:
    _hass: Incomplete
    _entry: Incomplete
    _peblar: Incomplete
    _retry: Incomplete
    _state: SessionState | None
    def __init__(self, hass: HomeAssistant, entry: PeblarConfigEntry, peblar: Peblar) -> None: ...
    async def async_run(self) -> None: ...
    async def _async_listen(self) -> None: ...
    @callback
    def _handle_session_status(self, status: PeblarSessionStatus) -> None: ...
