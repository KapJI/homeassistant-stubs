import datetime as dt
from .frame import report as report
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.sun import STATE_ABOVE_HORIZON as STATE_ABOVE_HORIZON, STATE_BELOW_HORIZON as STATE_BELOW_HORIZON
from homeassistant.const import STATE_CLOSED as STATE_CLOSED, STATE_HOME as STATE_HOME, STATE_LOCKED as STATE_LOCKED, STATE_NOT_HOME as STATE_NOT_HOME, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_OPEN as STATE_OPEN, STATE_UNKNOWN as STATE_UNKNOWN, STATE_UNLOCKED as STATE_UNLOCKED
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from homeassistant.loader import IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration, bind_hass as bind_hass
from types import TracebackType
from typing import Any

_LOGGER: Incomplete

class AsyncTrackStates:
    hass: Incomplete
    states: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    now: Incomplete
    def __enter__(self) -> list[State]: ...
    def __exit__(self, exc_type: Union[type[BaseException], None], exc_value: Union[BaseException, None], traceback: Union[TracebackType, None]) -> None: ...

def get_changed_since(states: Iterable[State], utc_point_in_time: dt.datetime) -> list[State]: ...
async def async_reproduce_state(hass: HomeAssistant, states: Union[State, Iterable[State]], *, context: Union[Context, None] = ..., reproduce_options: Union[dict[str, Any], None] = ...) -> None: ...
def state_as_number(state: State) -> float: ...
