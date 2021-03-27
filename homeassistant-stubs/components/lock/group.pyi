from homeassistant.components.group import GroupIntegrationRegistry as GroupIntegrationRegistry
from homeassistant.const import STATE_LOCKED as STATE_LOCKED, STATE_UNLOCKED as STATE_UNLOCKED
from homeassistant.core import callback as callback
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType

def async_describe_on_off_states(hass: HomeAssistantType, registry: GroupIntegrationRegistry) -> None: ...
