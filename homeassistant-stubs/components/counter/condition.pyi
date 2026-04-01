from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.condition import Condition as Condition, make_entity_numerical_condition as make_entity_numerical_condition

DOMAIN: str
CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
