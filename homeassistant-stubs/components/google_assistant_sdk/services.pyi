from .const import DOMAIN as DOMAIN
from .helpers import async_send_text_commands as async_send_text_commands
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback

SERVICE_SEND_TEXT_COMMAND: str
SERVICE_SEND_TEXT_COMMAND_FIELD_COMMAND: str
SERVICE_SEND_TEXT_COMMAND_FIELD_MEDIA_PLAYER: str
SERVICE_SEND_TEXT_COMMAND_SCHEMA: Incomplete

async def _send_text_command(call: ServiceCall) -> ServiceResponse: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
