from .const import AUTHORIZE_URL as AUTHORIZE_URL, TOKEN_URL as TOKEN_URL
from .oauth import TeslemetryImplementation as TeslemetryImplementation
from homeassistant.components.application_credentials import AuthorizationServer as AuthorizationServer, ClientCredential as ClientCredential
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow

async def async_get_authorization_server(hass: HomeAssistant) -> AuthorizationServer: ...
async def async_get_auth_implementation(hass: HomeAssistant, auth_domain: str, credential: ClientCredential) -> config_entry_oauth2_flow.AbstractOAuth2Implementation: ...
