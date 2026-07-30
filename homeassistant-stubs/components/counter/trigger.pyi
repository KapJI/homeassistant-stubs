from . import DOMAIN as DOMAIN
from .const import CounterEntityStateAttribute as CounterEntityStateAttribute
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.trigger import ENTITY_STATE_TRIGGER_SCHEMA as ENTITY_STATE_TRIGGER_SCHEMA, EntityTriggerBase as EntityTriggerBase, NotTriggeredReasonReporter as NotTriggeredReasonReporter, Trigger as Trigger
from typing import override

def _is_integer_state(state: State) -> bool: ...

class CounterBaseIntegerTrigger(EntityTriggerBase):
    _domain_specs: Incomplete
    _schema = ENTITY_STATE_TRIGGER_SCHEMA
    @override
    def is_valid_state(self, state: State, report_not_triggered: NotTriggeredReasonReporter) -> bool: ...

class CounterDecrementedTrigger(CounterBaseIntegerTrigger):
    @override
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...

class CounterIncrementedTrigger(CounterBaseIntegerTrigger):
    @override
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...

class CounterValueBaseTrigger(EntityTriggerBase):
    _domain_specs: Incomplete

class CounterMaxReachedTrigger(CounterValueBaseTrigger):
    @override
    def is_valid_state(self, state: State, report_not_triggered: NotTriggeredReasonReporter) -> bool: ...

class CounterMinReachedTrigger(CounterValueBaseTrigger):
    @override
    def is_valid_state(self, state: State, report_not_triggered: NotTriggeredReasonReporter) -> bool: ...

class CounterResetTrigger(CounterValueBaseTrigger):
    @override
    def is_valid_state(self, state: State, report_not_triggered: NotTriggeredReasonReporter) -> bool: ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
