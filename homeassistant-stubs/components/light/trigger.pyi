from . import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS
from .const import DOMAIN as DOMAIN
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.trigger import Trigger as Trigger, make_entity_numerical_state_attribute_changed_trigger as make_entity_numerical_state_attribute_changed_trigger, make_entity_numerical_state_attribute_crossed_threshold_trigger as make_entity_numerical_state_attribute_crossed_threshold_trigger, make_entity_target_state_trigger as make_entity_target_state_trigger

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
