from .const import ATTR_ACTION as ATTR_ACTION, DOMAIN as DOMAIN, HumidifierAction as HumidifierAction
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.trigger import Trigger as Trigger, make_entity_target_state_trigger as make_entity_target_state_trigger

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
