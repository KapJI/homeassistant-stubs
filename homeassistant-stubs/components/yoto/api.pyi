from _typeshed import Incomplete
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session
from typing import override
from yoto_api import AbstractAuth

class AsyncConfigEntryAuth(AbstractAuth):
    _oauth_session: Incomplete
    def __init__(self, oauth_session: OAuth2Session) -> None: ...
    @override
    async def async_get_access_token(self) -> str: ...
