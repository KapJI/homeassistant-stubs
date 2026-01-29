from .const import DOMAIN as DOMAIN
from .entity import AssistSatelliteState as AssistSatelliteState
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.condition import Condition as Condition, make_entity_state_condition as make_entity_state_condition

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
