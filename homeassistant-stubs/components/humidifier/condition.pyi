from .const import ATTR_ACTION as ATTR_ACTION, DOMAIN as DOMAIN, HumidifierAction as HumidifierAction
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.condition import Condition as Condition, make_entity_state_attribute_condition as make_entity_state_attribute_condition, make_entity_state_condition as make_entity_state_condition

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
