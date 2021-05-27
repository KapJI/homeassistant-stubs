from homeassistant.components.group import GroupIntegrationRegistry as GroupIntegrationRegistry
from homeassistant.const import STATE_HOME as STATE_HOME, STATE_NOT_HOME as STATE_NOT_HOME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def async_describe_on_off_states(hass: HomeAssistant, registry: GroupIntegrationRegistry) -> None: ...
