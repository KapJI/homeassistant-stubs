from .const import CONTROLLER as CONTROLLER
from aiohomekit import Controller
from homeassistant.components import zeroconf as zeroconf
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant

async def async_get_controller(hass: HomeAssistant) -> Controller: ...
