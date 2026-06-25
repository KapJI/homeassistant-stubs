from . import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS
from .const import DOMAIN as DOMAIN
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.trigger import EntityNumericalStateChangedTriggerBase as EntityNumericalStateChangedTriggerBase, EntityNumericalStateCrossedThresholdTriggerBase as EntityNumericalStateCrossedThresholdTriggerBase, EntityNumericalStateTriggerBase as EntityNumericalStateTriggerBase, Trigger as Trigger, make_entity_target_state_trigger as make_entity_target_state_trigger
from typing import override

BRIGHTNESS_DOMAIN_SPECS: dict[str, DomainSpec]

class BrightnessTriggerMixin(EntityNumericalStateTriggerBase):
    _domain_specs = BRIGHTNESS_DOMAIN_SPECS
    _valid_unit: str
    @override
    def _get_tracked_value(self, state: State) -> float | None: ...

class BrightnessChangedTrigger(EntityNumericalStateChangedTriggerBase, BrightnessTriggerMixin): ...
class BrightnessCrossedThresholdTrigger(EntityNumericalStateCrossedThresholdTriggerBase, BrightnessTriggerMixin): ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
