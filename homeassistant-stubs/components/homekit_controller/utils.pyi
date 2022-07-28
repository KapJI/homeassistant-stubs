from .const import CONTROLLER as CONTROLLER
from aiohomekit import Controller
from homeassistant.components import bluetooth as bluetooth, zeroconf as zeroconf
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant

def folded_name(name: str) -> str: ...
async def async_get_controller(hass: HomeAssistant) -> Controller: ...
