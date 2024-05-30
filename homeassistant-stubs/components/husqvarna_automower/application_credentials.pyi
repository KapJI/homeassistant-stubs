from .const import OAUTH2_AUTHORIZE as OAUTH2_AUTHORIZE, OAUTH2_TOKEN as OAUTH2_TOKEN
from homeassistant.components.application_credentials import AuthorizationServer as AuthorizationServer
from homeassistant.core import HomeAssistant as HomeAssistant

async def async_get_authorization_server(hass: HomeAssistant) -> AuthorizationServer: ...
