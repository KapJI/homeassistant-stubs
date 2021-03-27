from . import STATE_ECO as STATE_ECO, STATE_ELECTRIC as STATE_ELECTRIC, STATE_GAS as STATE_GAS, STATE_HEAT_PUMP as STATE_HEAT_PUMP, STATE_HIGH_DEMAND as STATE_HIGH_DEMAND, STATE_PERFORMANCE as STATE_PERFORMANCE
from homeassistant.components.group import GroupIntegrationRegistry as GroupIntegrationRegistry
from homeassistant.const import STATE_OFF as STATE_OFF
from homeassistant.core import callback as callback
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType

def async_describe_on_off_states(hass: HomeAssistantType, registry: GroupIntegrationRegistry) -> None: ...
