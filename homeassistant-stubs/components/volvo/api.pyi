from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session
from homeassistant.helpers.redact import async_redact_data as async_redact_data
from volvocarsapi.auth import AccessTokenManager

_LOGGER: Incomplete
_TO_REDACT: Incomplete

class VolvoAuth(AccessTokenManager):
    _oauth_session: Incomplete
    def __init__(self, websession: ClientSession, oauth_session: OAuth2Session) -> None: ...
    async def async_get_access_token(self) -> str: ...

class ConfigFlowVolvoAuth(AccessTokenManager):
    _token: Incomplete
    def __init__(self, websession: ClientSession, token: str) -> None: ...
    async def async_get_access_token(self) -> str: ...
