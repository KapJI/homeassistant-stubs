from homeassistant.core import HomeAssistant as HomeAssistant, split_entity_id as split_entity_id
from typing import Any

_LOGGER: Any

def is_on(hass: HomeAssistant, entity_id: Union[str, None] = ...) -> bool: ...
