from . import ATTR_IS_CLOSED as ATTR_IS_CLOSED
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.condition import Condition as Condition, make_entity_state_condition as make_entity_state_condition

VALVE_DOMAIN_SPECS: Incomplete
CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
