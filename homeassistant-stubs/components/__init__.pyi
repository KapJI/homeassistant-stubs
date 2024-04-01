from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, split_entity_id as split_entity_id
from homeassistant.helpers.frame import report as report
from homeassistant.helpers.group import expand_entity_ids as expand_entity_ids

_LOGGER: Incomplete

def is_on(hass: HomeAssistant, entity_id: str | None = None) -> bool: ...
