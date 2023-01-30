from . import OTBRData as OTBRData
from .const import DOMAIN as DOMAIN
from homeassistant.components.websocket_api import ActiveConnection as ActiveConnection, async_register_command as async_register_command, async_response as async_response, websocket_command as websocket_command
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

def async_setup(hass: HomeAssistant) -> None: ...
async def websocket_info(hass: HomeAssistant, connection: ActiveConnection, msg: dict) -> None: ...
