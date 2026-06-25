from homeassistant.components.application_credentials import ClientCredential as ClientCredential
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_entry_oauth2_flow import LocalOAuth2ImplementationWithPkce as LocalOAuth2ImplementationWithPkce
from typing import override

async def async_get_auth_implementation(hass: HomeAssistant, auth_domain: str, credential: ClientCredential) -> LocalOAuth2ImplementationWithPkce: ...

class OverkizOAuth2Implementation(LocalOAuth2ImplementationWithPkce):
    @property
    @override
    def extra_authorize_data(self) -> dict: ...
