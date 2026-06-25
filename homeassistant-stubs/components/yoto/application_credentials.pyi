from homeassistant.components.application_credentials import ClientCredential as ClientCredential
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_entry_oauth2_flow import LocalOAuth2ImplementationWithPkce as LocalOAuth2ImplementationWithPkce

AUTHORIZE_URL: str
TOKEN_URL: str

async def async_get_auth_implementation(hass: HomeAssistant, auth_domain: str, credential: ClientCredential) -> LocalOAuth2ImplementationWithPkce: ...
