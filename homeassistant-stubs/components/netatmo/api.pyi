import pyatmo
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow

class AsyncConfigEntryNetatmoAuth(pyatmo.AbstractAsyncAuth):
    _oauth_session: Incomplete
    def __init__(self, websession: ClientSession, oauth_session: config_entry_oauth2_flow.OAuth2Session) -> None: ...
    async def async_get_access_token(self) -> str: ...
