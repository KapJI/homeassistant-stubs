from .const import API_URL as API_URL, OAUTH2_TOKEN as OAUTH2_TOKEN, SDM_SCOPES as SDM_SCOPES
from aiohttp import ClientSession as ClientSession
from google.oauth2.credentials import Credentials
from google_nest_sdm.auth import AbstractAuth
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import Any

class AsyncConfigEntryAuth(AbstractAuth):
    _oauth_session: Any
    _client_id: Any
    _client_secret: Any
    def __init__(self, websession: ClientSession, oauth_session: config_entry_oauth2_flow.OAuth2Session, client_id: str, client_secret: str) -> None: ...
    async def async_get_access_token(self) -> str: ...
    async def async_get_creds(self) -> Credentials: ...
