from . import ATTR_MEDIA_VOLUME_LEVEL as ATTR_MEDIA_VOLUME_LEVEL, ATTR_MEDIA_VOLUME_MUTED as ATTR_MEDIA_VOLUME_MUTED
from .const import DOMAIN as DOMAIN, MediaPlayerState as MediaPlayerState
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.condition import Condition as Condition, EntityConditionBase as EntityConditionBase, EntityNumericalConditionBase as EntityNumericalConditionBase, make_entity_state_condition as make_entity_state_condition
from typing import Any

class _MediaPlayerMutedConditionBase(EntityConditionBase):
    _domain_specs: Incomplete
    _target_muted: bool
    def _state_valid_since(self, state: State) -> datetime: ...
    def _has_volume_attributes(self, state: State) -> bool: ...
    def _should_include(self, state: State) -> bool: ...
    def _is_muted(self, state: State) -> bool: ...
    def is_valid_state(self, entity_state: State) -> bool: ...

class MediaPlayerIsMutedCondition(_MediaPlayerMutedConditionBase):
    _target_muted: bool

class MediaPlayerIsUnmutedCondition(_MediaPlayerMutedConditionBase):
    _target_muted: bool

class MediaPlayerIsVolumeCondition(EntityNumericalConditionBase):
    _domain_specs: Incomplete
    _valid_unit: str
    def _get_tracked_value(self, entity_state: State) -> Any: ...
    def _should_include(self, state: State) -> bool: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
