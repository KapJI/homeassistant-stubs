import probatio
from .descriptions import TRIGGER_DESCRIPTION_CACHE as TRIGGER_DESCRIPTION_CACHE, async_get_all_descriptions as async_get_all_descriptions, starts_with_dot as starts_with_dot
from .entity_trigger import ATTR_BEHAVIOR as ATTR_BEHAVIOR, BEHAVIOR_ALL as BEHAVIOR_ALL, BEHAVIOR_EACH as BEHAVIOR_EACH, BEHAVIOR_FIRST as BEHAVIOR_FIRST, ENTITY_STATE_TRIGGER_SCHEMA as ENTITY_STATE_TRIGGER_SCHEMA, ENTITY_STATE_TRIGGER_SCHEMA_WITH_BEHAVIOR as ENTITY_STATE_TRIGGER_SCHEMA_WITH_BEHAVIOR, EntityNumericalStateChangedTriggerBase as EntityNumericalStateChangedTriggerBase, EntityNumericalStateChangedTriggerWithUnitBase as EntityNumericalStateChangedTriggerWithUnitBase, EntityNumericalStateCrossedThresholdTriggerBase as EntityNumericalStateCrossedThresholdTriggerBase, EntityNumericalStateCrossedThresholdTriggerWithUnitBase as EntityNumericalStateCrossedThresholdTriggerWithUnitBase, EntityNumericalStateTriggerBase as EntityNumericalStateTriggerBase, EntityNumericalStateTriggerWithUnitBase as EntityNumericalStateTriggerWithUnitBase, EntityOriginStateTriggerBase as EntityOriginStateTriggerBase, EntityTargetStateTriggerBase as EntityTargetStateTriggerBase, EntityTransitionTriggerBase as EntityTransitionTriggerBase, EntityTriggerBase as EntityTriggerBase, NUMERICAL_ATTRIBUTE_CHANGED_TRIGGER_SCHEMA as NUMERICAL_ATTRIBUTE_CHANGED_TRIGGER_SCHEMA, NUMERICAL_ATTRIBUTE_CROSSED_THRESHOLD_SCHEMA as NUMERICAL_ATTRIBUTE_CROSSED_THRESHOLD_SCHEMA, NotTriggeredReasonReporter as NotTriggeredReasonReporter, StatelessEntityTriggerBase as StatelessEntityTriggerBase, make_entity_numerical_state_changed_trigger as make_entity_numerical_state_changed_trigger, make_entity_numerical_state_changed_with_unit_trigger as make_entity_numerical_state_changed_with_unit_trigger, make_entity_numerical_state_crossed_threshold_trigger as make_entity_numerical_state_crossed_threshold_trigger, make_entity_numerical_state_crossed_threshold_with_unit_trigger as make_entity_numerical_state_crossed_threshold_with_unit_trigger, make_entity_origin_state_trigger as make_entity_origin_state_trigger, make_entity_target_state_trigger as make_entity_target_state_trigger, make_entity_transition_trigger as make_entity_transition_trigger, make_numerical_state_changed_with_unit_schema as make_numerical_state_changed_with_unit_schema
from .models import NotTriggeredInfo as NotTriggeredInfo, TRIGGERS as TRIGGERS, Trigger as Trigger, TriggerAction as TriggerAction, TriggerActionPayloadBuilder as TriggerActionPayloadBuilder, TriggerActionRunner as TriggerActionRunner, TriggerConfig as TriggerConfig, TriggerNotTriggeredReporter as TriggerNotTriggeredReporter
from _typeshed import Incomplete
from collections import defaultdict
from collections.abc import Callable, Coroutine
from dataclasses import dataclass, field
from homeassistant.core import CALLBACK_TYPE, Context, HassJob, HomeAssistant, callback
from homeassistant.helpers.typing import ConfigType, TemplateVarsType, UndefinedType
from homeassistant.util.hass_dict import HassKey
from typing import Any, Literal, Protocol, TypedDict

__all__ = ['ATTR_BEHAVIOR', 'BEHAVIOR_ALL', 'BEHAVIOR_EACH', 'BEHAVIOR_FIRST', 'DATA_PLUGGABLE_ACTIONS', 'ENTITY_STATE_TRIGGER_SCHEMA', 'ENTITY_STATE_TRIGGER_SCHEMA_WITH_BEHAVIOR', 'NUMERICAL_ATTRIBUTE_CHANGED_TRIGGER_SCHEMA', 'NUMERICAL_ATTRIBUTE_CROSSED_THRESHOLD_SCHEMA', 'TRIGGERS', 'TRIGGER_DESCRIPTION_CACHE', 'TRIGGER_PLATFORM_SUBSCRIPTIONS', 'EntityNumericalStateChangedTriggerBase', 'EntityNumericalStateChangedTriggerWithUnitBase', 'EntityNumericalStateCrossedThresholdTriggerBase', 'EntityNumericalStateCrossedThresholdTriggerWithUnitBase', 'EntityNumericalStateTriggerBase', 'EntityNumericalStateTriggerWithUnitBase', 'EntityOriginStateTriggerBase', 'EntityTargetStateTriggerBase', 'EntityTransitionTriggerBase', 'EntityTriggerBase', 'NotTriggeredInfo', 'NotTriggeredReasonReporter', 'PluggableAction', 'PluggableActionsEntry', 'StatelessEntityTriggerBase', 'Trigger', 'TriggerAction', 'TriggerActionPayloadBuilder', 'TriggerActionRunner', 'TriggerActionType', 'TriggerConfig', 'TriggerData', 'TriggerInfo', 'TriggerNotTriggeredAction', 'TriggerNotTriggeredReporter', 'TriggerProtocol', 'async_extract_devices', 'async_extract_entities', 'async_extract_targets', 'async_get_all_descriptions', 'async_initialize_triggers', 'async_setup', 'async_subscribe_platform_events', 'async_validate_trigger_config', 'make_entity_numerical_state_changed_trigger', 'make_entity_numerical_state_changed_with_unit_trigger', 'make_entity_numerical_state_crossed_threshold_trigger', 'make_entity_numerical_state_crossed_threshold_with_unit_trigger', 'make_entity_origin_state_trigger', 'make_entity_target_state_trigger', 'make_entity_transition_trigger', 'make_numerical_state_changed_with_unit_schema', 'starts_with_dot']

DATA_PLUGGABLE_ACTIONS: HassKey[defaultdict[tuple, PluggableActionsEntry]]
TRIGGER_PLATFORM_SUBSCRIPTIONS: HassKey[list[Callable[[set[str]], Coroutine[Any, Any, None]]]]

async def async_setup(hass: HomeAssistant) -> None: ...
@callback
def async_subscribe_platform_events(hass: HomeAssistant, on_event: Callable[[set[str]], Coroutine[Any, Any, None]]) -> Callable[[], None]: ...

class TriggerProtocol(Protocol):
    async def async_get_triggers(self, hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
    TRIGGER_SCHEMA: probatio.Schema
    async def async_validate_trigger_config(self, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    async def async_attach_trigger(self, hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...

class TriggerNotTriggeredAction(Protocol):
    @callback
    def __call__(self, run_variables: dict[str, Any], info: NotTriggeredInfo, context: Context | None = None) -> None: ...

class TriggerActionType(Protocol):
    def __call__(self, run_variables: dict[str, Any], context: Context | None = None) -> Coroutine[Any, Any, Any] | Any: ...

class TriggerData(TypedDict):
    id: str
    idx: str
    alias: str | None

class TriggerInfo(TypedDict):
    domain: str
    name: str
    variables: TemplateVarsType
    trigger_data: TriggerData

@dataclass(slots=True)
class PluggableActionsEntry:
    plugs: set[PluggableAction] = field(default_factory=set)
    actions: dict[object, tuple[HassJob[[dict[str, Any], Context | None], Coroutine[Any, Any, None] | Any], dict[str, Any]]] = field(default_factory=dict)

class PluggableAction:
    _entry: PluggableActionsEntry | None
    _update: Incomplete
    def __init__(self, update: CALLBACK_TYPE | None = None) -> None: ...
    def __bool__(self) -> bool: ...
    @callback
    def async_run_update(self) -> None: ...
    @staticmethod
    @callback
    def async_get_registry(hass: HomeAssistant) -> dict[tuple, PluggableActionsEntry]: ...
    @staticmethod
    @callback
    def async_attach_trigger(hass: HomeAssistant, trigger: dict[str, str], action: TriggerActionType, variables: dict[str, Any]) -> CALLBACK_TYPE: ...
    @callback
    def async_register(self, hass: HomeAssistant, trigger: dict[str, str]) -> CALLBACK_TYPE: ...
    async def async_run(self, hass: HomeAssistant, context: Context | None = None) -> None: ...

async def async_validate_trigger_config(hass: HomeAssistant, trigger_config: list[ConfigType]) -> list[ConfigType]: ...
async def async_initialize_triggers(hass: HomeAssistant, trigger_config: list[ConfigType], action: Callable, domain: str, name: str, log_cb: Callable, home_assistant_start: bool | UndefinedType = ..., variables: TemplateVarsType = None, *, did_not_trigger: TriggerNotTriggeredAction | None = None) -> CALLBACK_TYPE | None: ...
@callback
def async_extract_devices(trigger_conf: dict) -> list[str]: ...
@callback
def async_extract_entities(trigger_conf: dict) -> list[str]: ...
@callback
def async_extract_targets(config: dict, target: Literal['entity_id', 'device_id', 'area_id', 'floor_id', 'label_id']) -> list[str]: ...
