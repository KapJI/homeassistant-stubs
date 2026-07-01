from . import ATTR_MEDIA_VOLUME_LEVEL as ATTR_MEDIA_VOLUME_LEVEL, ATTR_MEDIA_VOLUME_MUTED as ATTR_MEDIA_VOLUME_MUTED, MediaPlayerState as MediaPlayerState
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.trigger import EntityNumericalStateChangedTriggerBase as EntityNumericalStateChangedTriggerBase, EntityNumericalStateCrossedThresholdTriggerBase as EntityNumericalStateCrossedThresholdTriggerBase, EntityNumericalStateTriggerBase as EntityNumericalStateTriggerBase, EntityTriggerBase as EntityTriggerBase, NotTriggeredReasonReporter as NotTriggeredReasonReporter, Trigger as Trigger, make_entity_transition_trigger as make_entity_transition_trigger
from typing import override

VOLUME_DOMAIN_SPECS: dict[str, DomainSpec]

class _MediaPlayerMutedStateTriggerBase(EntityTriggerBase):
    _domain_specs: Incomplete
    _target_muted: bool
    def _has_volume_attributes(self, state: State) -> bool: ...
    @override
    def _should_include(self, state: State) -> bool: ...
    def is_muted(self, state: State) -> bool: ...
    @override
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...
    @override
    def is_valid_state(self, state: State, report_not_triggered: NotTriggeredReasonReporter) -> bool: ...

class MediaPlayerMutedTrigger(_MediaPlayerMutedStateTriggerBase):
    _target_muted: bool

class MediaPlayerUnmutedTrigger(_MediaPlayerMutedStateTriggerBase):
    _target_muted: bool

class VolumeTriggerMixin(EntityNumericalStateTriggerBase):
    _domain_specs = VOLUME_DOMAIN_SPECS
    _valid_unit: str
    @override
    def _get_tracked_value(self, state: State) -> float | None: ...
    @override
    def _should_include(self, state: State) -> bool: ...

class VolumeChangedTrigger(EntityNumericalStateChangedTriggerBase, VolumeTriggerMixin): ...
class VolumeCrossedThresholdTrigger(EntityNumericalStateCrossedThresholdTriggerBase, VolumeTriggerMixin): ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
