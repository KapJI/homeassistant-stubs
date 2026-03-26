import abc
from . import CONF_INITIAL as CONF_INITIAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import CONF_MAXIMUM as CONF_MAXIMUM, CONF_MINIMUM as CONF_MINIMUM, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.trigger import ENTITY_STATE_TRIGGER_SCHEMA as ENTITY_STATE_TRIGGER_SCHEMA, EntityTriggerBase as EntityTriggerBase, Trigger as Trigger

def _is_integer_state(state: State) -> bool: ...

class CounterBaseIntegerTrigger(EntityTriggerBase, metaclass=abc.ABCMeta):
    _domain_specs: Incomplete
    _schema = ENTITY_STATE_TRIGGER_SCHEMA
    def is_valid_state(self, state: State) -> bool: ...

class CounterDecrementedTrigger(CounterBaseIntegerTrigger):
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...

class CounterIncrementedTrigger(CounterBaseIntegerTrigger):
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...

class CounterValueBaseTrigger(EntityTriggerBase, metaclass=abc.ABCMeta):
    _domain_specs: Incomplete
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...

class CounterMaxReachedTrigger(CounterValueBaseTrigger):
    def is_valid_state(self, state: State) -> bool: ...

class CounterMinReachedTrigger(CounterValueBaseTrigger):
    def is_valid_state(self, state: State) -> bool: ...

class CounterResetTrigger(CounterValueBaseTrigger):
    def is_valid_state(self, state: State) -> bool: ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
