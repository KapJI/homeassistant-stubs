from .const import DATA_CLOUD as DATA_CLOUD, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import OAuth2TokenRequestError as OAuth2TokenRequestError, OAuth2TokenRequestReauthError as OAuth2TokenRequestReauthError, OAuth2TokenRequestTransientError as OAuth2TokenRequestTransientError
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow, event as event
from typing import Any, override

DATA_SERVICES: str
CACHE_TIMEOUT: int
_LOGGER: Incomplete
CURRENT_VERSION: Incomplete
CURRENT_PLAIN_VERSION: Incomplete

@callback
def async_setup(hass: HomeAssistant) -> None: ...
async def async_provide_implementation(hass: HomeAssistant, domain: str) -> list[config_entry_oauth2_flow.AbstractOAuth2Implementation]: ...
async def _get_services(hass: HomeAssistant) -> list[dict[str, Any]]: ...

class CloudOAuth2Implementation(config_entry_oauth2_flow.AbstractOAuth2Implementation):
    hass: Incomplete
    service: Incomplete
    def __init__(self, hass: HomeAssistant, service: str) -> None: ...
    @property
    @override
    def name(self) -> str: ...
    @property
    @override
    def domain(self) -> str: ...
    @override
    async def async_generate_authorize_url(self, flow_id: str) -> str: ...
    @override
    async def async_resolve_external_data(self, external_data: Any) -> dict: ...
    @override
    async def _async_refresh_token(self, token: dict) -> dict: ...
