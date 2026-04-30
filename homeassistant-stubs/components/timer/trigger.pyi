from . import ATTR_LAST_TRANSITION as ATTR_LAST_TRANSITION, DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.trigger import Trigger as Trigger, make_entity_target_state_trigger as make_entity_target_state_trigger

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
