import voluptuous as vol
from . import condition as condition
from .condition import _IN_ZONES_DOMAINS as _IN_ZONES_DOMAINS
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.device_tracker import ATTR_IN_ZONES as ATTR_IN_ZONES
from homeassistant.const import ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_EVENT as CONF_EVENT, CONF_FOR as CONF_FOR, CONF_OPTIONS as CONF_OPTIONS, CONF_TARGET as CONF_TARGET, CONF_ZONE as CONF_ZONE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers import location as location
from homeassistant.helpers.automation import DomainSpec as DomainSpec, move_top_level_schema_fields_to_options as move_top_level_schema_fields_to_options
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.trigger import ENTITY_STATE_TRIGGER_SCHEMA_WITH_BEHAVIOR as ENTITY_STATE_TRIGGER_SCHEMA_WITH_BEHAVIOR, EntityTriggerBase as EntityTriggerBase, Trigger as Trigger, TriggerActionRunner as TriggerActionRunner, TriggerConfig as TriggerConfig, TriggerNotTriggeredReporter as TriggerNotTriggeredReporter
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, override

EVENT_ENTER: str
EVENT_LEAVE: str
DEFAULT_EVENT = EVENT_ENTER
_LOGGER: Incomplete
_EVENT_DESCRIPTION: Incomplete

def _state_has_zone_info(state: State) -> bool: ...

_LEGACY_OPTIONS_SCHEMA: dict[vol.Marker, Any]
_LEGACY_TRIGGER_OPTIONS_SCHEMA: Incomplete
_ZONE_TRIGGER_SCHEMA: Incomplete
_DOMAIN_SPECS: dict[str, DomainSpec]

class LegacyZoneTrigger(Trigger):
    @classmethod
    @override
    async def async_validate_complete_config(cls, hass: HomeAssistant, complete_config: ConfigType) -> ConfigType: ...
    @classmethod
    @override
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    _options: Incomplete
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    @override
    async def async_attach_runner(self, run_action: TriggerActionRunner, did_not_trigger: TriggerNotTriggeredReporter | None = None) -> CALLBACK_TYPE: ...

class ZoneTriggerBase(EntityTriggerBase):
    _domain_specs = _DOMAIN_SPECS
    _schema = _ZONE_TRIGGER_SCHEMA
    _zone: str
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    def _in_target_zone(self, state: State) -> bool: ...

class EnteredZoneTrigger(ZoneTriggerBase):
    @override
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...
    @override
    def is_valid_state(self, state: State) -> bool: ...

class LeftZoneTrigger(ZoneTriggerBase):
    @override
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...
    @override
    def is_valid_state(self, state: State) -> bool: ...

_OCCUPANCY_TRIGGER_SCHEMA: Incomplete

class _ZoneOccupancyTriggerBase(EntityTriggerBase):
    _domain_specs: Incomplete
    _schema = _OCCUPANCY_TRIGGER_SCHEMA
    @classmethod
    @override
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    @staticmethod
    def _occupancy_count(state: State) -> int | None: ...
    @classmethod
    def _is_occupied(cls, state: State) -> bool: ...

class OccupancyDetectedTrigger(_ZoneOccupancyTriggerBase):
    @override
    def is_valid_state(self, state: State) -> bool: ...
    @override
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...

class OccupancyClearedTrigger(_ZoneOccupancyTriggerBase):
    @override
    def is_valid_state(self, state: State) -> bool: ...
    @override
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
