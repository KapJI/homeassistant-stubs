from . import DOMAIN as DOMAIN, STATUS_ACTIVE as STATUS_ACTIVE, STATUS_IDLE as STATUS_IDLE, STATUS_PAUSED as STATUS_PAUSED
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.condition import Condition as Condition, make_entity_state_condition as make_entity_state_condition

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
