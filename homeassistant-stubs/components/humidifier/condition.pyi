from .const import ATTR_ACTION as ATTR_ACTION, ATTR_HUMIDITY as ATTR_HUMIDITY, DOMAIN as DOMAIN, HumidifierAction as HumidifierAction
from homeassistant.const import PERCENTAGE as PERCENTAGE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.automation import DomainSpec as DomainSpec, NumericalDomainSpec as NumericalDomainSpec
from homeassistant.helpers.condition import Condition as Condition, make_entity_numerical_condition as make_entity_numerical_condition, make_entity_state_condition as make_entity_state_condition

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
