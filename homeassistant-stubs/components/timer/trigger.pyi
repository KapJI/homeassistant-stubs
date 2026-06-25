from . import ATTR_FINISHES_AT as ATTR_FINISHES_AT, ATTR_LAST_TRANSITION as ATTR_LAST_TRANSITION, DOMAIN as DOMAIN, STATUS_ACTIVE as STATUS_ACTIVE
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_OPTIONS as CONF_OPTIONS
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Context as Context, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers.automation import DomainSpec as DomainSpec, filter_by_domain_specs as filter_by_domain_specs
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time
from homeassistant.helpers.target import TargetStateChangedData as TargetStateChangedData, async_track_target_selector_state_change_event as async_track_target_selector_state_change_event
from homeassistant.helpers.trigger import ENTITY_STATE_TRIGGER_SCHEMA as ENTITY_STATE_TRIGGER_SCHEMA, Trigger as Trigger, TriggerActionRunner as TriggerActionRunner, TriggerConfig as TriggerConfig, TriggerNotTriggeredReporter as TriggerNotTriggeredReporter, make_entity_target_state_trigger as make_entity_target_state_trigger
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import override

CONF_REMAINING: str
TIME_REMAINING_TRIGGER_SCHEMA: Incomplete

class TimeRemainingTrigger(Trigger):
    _domain_specs: dict[str, DomainSpec]
    _schema = TIME_REMAINING_TRIGGER_SCHEMA
    @override
    @classmethod
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    _target: Incomplete
    _remaining: timedelta
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    def entity_filter(self, entities: set[str]) -> set[str]: ...
    @override
    async def async_attach_runner(self, run_action: TriggerActionRunner, did_not_trigger: TriggerNotTriggeredReporter | None = None) -> CALLBACK_TYPE: ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
