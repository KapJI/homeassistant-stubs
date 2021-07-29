import pyatmo
from aiohttp import ClientSession as ClientSession
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import Any

class AsyncConfigEntryNetatmoAuth(pyatmo.auth.AbstractAsyncAuth):
    _oauth_session: Any
    def __init__(self, websession: ClientSession, oauth_session: config_entry_oauth2_flow.OAuth2Session) -> None: ...
    async def async_get_access_token(self) -> str: ...
