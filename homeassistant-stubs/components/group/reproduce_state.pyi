from . import get_entity_ids as get_entity_ids
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.state import async_reproduce_state as async_reproduce_state
from typing import Any, Iterable

async def async_reproduce_states(hass: HomeAssistant, states: Iterable[State], *, context: Union[Context, None]=..., reproduce_options: Union[dict[str, Any], None]=...) -> None: ...
