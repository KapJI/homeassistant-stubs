from .const import DOMAIN as DOMAIN, ValveEntityStateAttribute as ValveEntityStateAttribute
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.condition import Condition as Condition, make_entity_state_condition as make_entity_state_condition

VALVE_DOMAIN_SPECS: dict[str, DomainSpec]
CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
