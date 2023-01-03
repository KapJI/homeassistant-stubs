from _typeshed import Incomplete
from homeassistant.components.application_credentials import AuthorizationServer as AuthorizationServer
from homeassistant.core import HomeAssistant as HomeAssistant

AUTHORIZATION_SERVER: Incomplete

async def async_get_authorization_server(hass: HomeAssistant) -> AuthorizationServer: ...
async def async_get_description_placeholders(hass: HomeAssistant) -> dict[str, str]: ...
