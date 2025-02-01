from homeassistant.components.application_credentials import AuthorizationServer as AuthorizationServer
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow

async def async_get_authorization_server(hass: HomeAssistant) -> AuthorizationServer: ...
async def async_get_description_placeholders(hass: HomeAssistant) -> dict[str, str]: ...
