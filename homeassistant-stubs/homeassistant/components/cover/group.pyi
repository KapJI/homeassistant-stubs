from homeassistant.components.group import GroupIntegrationRegistry as GroupIntegrationRegistry
from homeassistant.const import STATE_CLOSED as STATE_CLOSED, STATE_OPEN as STATE_OPEN
from homeassistant.core import callback as callback
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType

def async_describe_on_off_states(hass: HomeAssistantType, registry: GroupIntegrationRegistry) -> None: ...
