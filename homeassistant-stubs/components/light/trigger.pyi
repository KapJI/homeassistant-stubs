import abc
from . import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.trigger import EntityNumericalStateChangedTriggerBase as EntityNumericalStateChangedTriggerBase, EntityNumericalStateCrossedThresholdTriggerBase as EntityNumericalStateCrossedThresholdTriggerBase, EntityNumericalStateTriggerBase as EntityNumericalStateTriggerBase, Trigger as Trigger, make_entity_target_state_trigger as make_entity_target_state_trigger

BRIGHTNESS_DOMAIN_SPECS: Incomplete

class BrightnessTriggerMixin(EntityNumericalStateTriggerBase, metaclass=abc.ABCMeta):
    _domain_specs = BRIGHTNESS_DOMAIN_SPECS
    _valid_unit: str
    def _get_tracked_value(self, state: State) -> float | None: ...

class BrightnessChangedTrigger(EntityNumericalStateChangedTriggerBase, BrightnessTriggerMixin): ...
class BrightnessCrossedThresholdTrigger(EntityNumericalStateCrossedThresholdTriggerBase, BrightnessTriggerMixin): ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
