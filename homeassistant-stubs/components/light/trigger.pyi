from . import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.trigger import EntityNumericalStateAttributeChangedTriggerBase as EntityNumericalStateAttributeChangedTriggerBase, EntityNumericalStateAttributeCrossedThresholdTriggerBase as EntityNumericalStateAttributeCrossedThresholdTriggerBase, Trigger as Trigger, make_entity_target_state_trigger as make_entity_target_state_trigger
from typing import Any

def _convert_uint8_to_percentage(value: Any) -> float: ...

class BrightnessChangedTrigger(EntityNumericalStateAttributeChangedTriggerBase):
    _domain = DOMAIN
    _attribute = ATTR_BRIGHTNESS
    _converter: Incomplete

class BrightnessCrossedThresholdTrigger(EntityNumericalStateAttributeCrossedThresholdTriggerBase):
    _domain = DOMAIN
    _attribute = ATTR_BRIGHTNESS
    _converter: Incomplete

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
