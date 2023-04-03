from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, SERVICE_LOCK as SERVICE_LOCK, SERVICE_UNLOCK as SERVICE_UNLOCK, STATE_LOCKED as STATE_LOCKED, STATE_LOCKING as STATE_LOCKING, STATE_UNLOCKED as STATE_UNLOCKED, STATE_UNLOCKING as STATE_UNLOCKING
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from typing import Any

_LOGGER: Incomplete
VALID_STATES: Incomplete

async def _async_reproduce_state(hass: HomeAssistant, state: State, *, context: Context | None = ..., reproduce_options: dict[str, Any] | None = ...) -> None: ...
async def async_reproduce_states(hass: HomeAssistant, states: Iterable[State], *, context: Context | None = ..., reproduce_options: dict[str, Any] | None = ...) -> None: ...
