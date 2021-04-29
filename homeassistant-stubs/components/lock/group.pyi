from homeassistant.components.group import GroupIntegrationRegistry as GroupIntegrationRegistry
from homeassistant.const import STATE_LOCKED as STATE_LOCKED, STATE_UNLOCKED as STATE_UNLOCKED
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def async_describe_on_off_states(hass: HomeAssistant, registry: GroupIntegrationRegistry) -> None: ...
