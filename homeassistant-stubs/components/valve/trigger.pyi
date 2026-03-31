from . import ATTR_IS_CLOSED as ATTR_IS_CLOSED, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.trigger import Trigger as Trigger, make_entity_transition_trigger as make_entity_transition_trigger

VALVE_DOMAIN_SPECS: Incomplete
TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
