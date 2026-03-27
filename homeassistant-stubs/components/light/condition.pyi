from . import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.condition import Condition as Condition, EntityNumericalConditionBase as EntityNumericalConditionBase, make_entity_state_condition as make_entity_state_condition
from typing import Any

BRIGHTNESS_DOMAIN_SPECS: Incomplete

class BrightnessCondition(EntityNumericalConditionBase):
    _domain_specs = BRIGHTNESS_DOMAIN_SPECS
    _valid_unit: str
    def _get_tracked_value(self, entity_state: State) -> Any: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
