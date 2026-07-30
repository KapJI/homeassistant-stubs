from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from google_health_api.auth import AbstractAuth
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import override

class AsyncConfigEntryAuth(AbstractAuth):
    _oauth_session: Incomplete
    def __init__(self, websession: ClientSession, oauth_session: config_entry_oauth2_flow.OAuth2Session) -> None: ...
    @override
    async def async_get_access_token(self) -> str: ...

class SimpleAuth(AbstractAuth):
    _access_token: Incomplete
    def __init__(self, websession: ClientSession, access_token: str) -> None: ...
    @override
    async def async_get_access_token(self) -> str: ...
