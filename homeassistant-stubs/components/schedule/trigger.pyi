from .const import ATTR_NEXT_EVENT as ATTR_NEXT_EVENT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.trigger import EntityTransitionTriggerBase as EntityTransitionTriggerBase, Trigger as Trigger, make_entity_target_state_trigger as make_entity_target_state_trigger

class ScheduleBackToBackTrigger(EntityTransitionTriggerBase):
    _domain_specs: Incomplete
    _from_states: Incomplete
    _to_states: Incomplete
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
