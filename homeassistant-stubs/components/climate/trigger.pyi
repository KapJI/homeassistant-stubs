from .const import ATTR_HVAC_ACTION as ATTR_HVAC_ACTION, DOMAIN as DOMAIN, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.trigger import Trigger as Trigger, make_conditional_entity_state_trigger as make_conditional_entity_state_trigger, make_entity_state_attribute_trigger as make_entity_state_attribute_trigger, make_entity_state_trigger as make_entity_state_trigger

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
