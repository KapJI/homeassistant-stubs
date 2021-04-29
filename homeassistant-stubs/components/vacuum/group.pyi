from . import STATE_CLEANING as STATE_CLEANING, STATE_ERROR as STATE_ERROR, STATE_RETURNING as STATE_RETURNING
from homeassistant.components.group import GroupIntegrationRegistry as GroupIntegrationRegistry
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def async_describe_on_off_states(hass: HomeAssistant, registry: GroupIntegrationRegistry) -> None: ...
