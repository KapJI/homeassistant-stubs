from .const import DOMAIN as DOMAIN
from homeassistant.components.group import GroupIntegrationRegistry as GroupIntegrationRegistry
from homeassistant.const import STATE_LOCKED as STATE_LOCKED, STATE_LOCKING as STATE_LOCKING, STATE_OPEN as STATE_OPEN, STATE_OPENING as STATE_OPENING, STATE_UNLOCKED as STATE_UNLOCKED, STATE_UNLOCKING as STATE_UNLOCKING
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def async_describe_on_off_states(hass: HomeAssistant, registry: GroupIntegrationRegistry) -> None: ...
