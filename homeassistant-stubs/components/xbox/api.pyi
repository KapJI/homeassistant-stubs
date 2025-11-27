from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session
from homeassistant.util.dt import utc_from_timestamp as utc_from_timestamp
from httpx import AsyncClient as AsyncClient
from pythonxbox.authentication.manager import AuthenticationManager
from pythonxbox.authentication.models import OAuth2TokenResponse

class AsyncConfigEntryAuth(AuthenticationManager):
    _oauth_session: Incomplete
    oauth: Incomplete
    def __init__(self, session: AsyncClient, oauth_session: OAuth2Session) -> None: ...
    async def refresh_tokens(self) -> None: ...
    def _get_oauth_token(self) -> OAuth2TokenResponse: ...
