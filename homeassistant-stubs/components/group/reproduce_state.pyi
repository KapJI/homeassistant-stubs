from . import get_entity_ids as get_entity_ids
from homeassistant.core import Context as Context, State as State
from homeassistant.helpers.state import async_reproduce_state as async_reproduce_state
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType
from typing import Any, Dict, Iterable, Optional

async def async_reproduce_states(hass: HomeAssistantType, states: Iterable[State], *, context: Optional[Context]=..., reproduce_options: Optional[Dict[str, Any]]=...) -> None: ...
