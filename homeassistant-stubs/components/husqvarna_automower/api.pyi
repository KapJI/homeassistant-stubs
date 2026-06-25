from _typeshed import Incomplete
from aioautomower.auth import AbstractAuth
from aiohttp import ClientSession as ClientSession
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import override

_LOGGER: Incomplete

class AsyncConfigEntryAuth(AbstractAuth):
    _oauth_session: Incomplete
    def __init__(self, websession: ClientSession, oauth_session: config_entry_oauth2_flow.OAuth2Session) -> None: ...
    @override
    async def async_get_access_token(self) -> str: ...

class AsyncConfigFlowAuth(AbstractAuth):
    token: dict
    def __init__(self, websession: ClientSession, token: dict) -> None: ...
    @override
    async def async_get_access_token(self) -> str: ...
