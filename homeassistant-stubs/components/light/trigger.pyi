from . import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.automation import NumericalDomainSpec as NumericalDomainSpec
from homeassistant.helpers.trigger import Trigger as Trigger, make_entity_numerical_state_changed_trigger as make_entity_numerical_state_changed_trigger, make_entity_numerical_state_crossed_threshold_trigger as make_entity_numerical_state_crossed_threshold_trigger, make_entity_target_state_trigger as make_entity_target_state_trigger
from typing import Any

def _convert_uint8_to_percentage(value: Any) -> float: ...

BRIGHTNESS_DOMAIN_SPECS: Incomplete
TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
