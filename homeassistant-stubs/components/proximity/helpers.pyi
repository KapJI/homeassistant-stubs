from homeassistant.components.automation import automations_with_entity as automations_with_entity
from homeassistant.components.script import scripts_with_entity as scripts_with_entity
from homeassistant.core import HomeAssistant as HomeAssistant

def entity_used_in(hass: HomeAssistant, entity_id: str) -> list[str]: ...
