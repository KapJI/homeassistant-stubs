from . import ATTR_OPTION as ATTR_OPTION, ATTR_OPTIONS as ATTR_OPTIONS, DOMAIN as DOMAIN, SERVICE_SELECT_OPTION as SERVICE_SELECT_OPTION, SERVICE_SET_OPTIONS as SERVICE_SET_OPTIONS
from collections.abc import Iterable
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from types import MappingProxyType
from typing import Any

ATTR_GROUP: Any
_LOGGER: Any

async def _async_reproduce_state(hass: HomeAssistant, state: State, *, context: Union[Context, None] = ..., reproduce_options: Union[dict[str, Any], None] = ...) -> None: ...
async def async_reproduce_states(hass: HomeAssistant, states: Iterable[State], *, context: Union[Context, None] = ..., reproduce_options: Union[dict[str, Any], None] = ...) -> None: ...
def check_attr_equal(attr1: MappingProxyType, attr2: MappingProxyType, attr_str: str) -> bool: ...
