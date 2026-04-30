from .const import OAUTH2_AUTHORIZE as OAUTH2_AUTHORIZE, OAUTH2_SCOPES as OAUTH2_SCOPES, OAUTH2_TOKEN as OAUTH2_TOKEN
from homeassistant.components.application_credentials import ClientCredential as ClientCredential
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_entry_oauth2_flow import AbstractOAuth2Implementation as AbstractOAuth2Implementation, LocalOAuth2ImplementationWithPkce as LocalOAuth2ImplementationWithPkce

async def async_get_auth_implementation(hass: HomeAssistant, auth_domain: str, credential: ClientCredential) -> AbstractOAuth2Implementation: ...

class DropboxOAuth2Implementation(LocalOAuth2ImplementationWithPkce):
    @property
    def extra_authorize_data(self) -> dict: ...
