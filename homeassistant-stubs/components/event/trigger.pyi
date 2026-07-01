from .const import ATTR_EVENT_TYPE as ATTR_EVENT_TYPE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import CONF_OPTIONS as CONF_OPTIONS
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.trigger import ENTITY_STATE_TRIGGER_SCHEMA as ENTITY_STATE_TRIGGER_SCHEMA, NotTriggeredReasonReporter as NotTriggeredReasonReporter, StatelessEntityTriggerBase as StatelessEntityTriggerBase, Trigger as Trigger, TriggerConfig as TriggerConfig
from typing import override

CONF_EVENT_TYPE: str
EVENT_RECEIVED_TRIGGER_SCHEMA: Incomplete

class EventReceivedTrigger(StatelessEntityTriggerBase):
    _domain_specs: Incomplete
    _schema = EVENT_RECEIVED_TRIGGER_SCHEMA
    _event_types: Incomplete
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    @override
    def is_valid_state(self, state: State, report_not_triggered: NotTriggeredReasonReporter) -> bool: ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
