from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.trigger import Trigger as Trigger, make_entity_target_state_trigger as make_entity_target_state_trigger

SWITCH_DOMAIN_SPECS: Incomplete
TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
