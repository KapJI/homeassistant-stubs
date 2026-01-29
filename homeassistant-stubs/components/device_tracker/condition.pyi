from .const import DOMAIN as DOMAIN
from homeassistant.const import STATE_HOME as STATE_HOME, STATE_NOT_HOME as STATE_NOT_HOME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.condition import Condition as Condition, make_entity_state_condition as make_entity_state_condition

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
