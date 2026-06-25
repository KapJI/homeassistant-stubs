from _typeshed import Incomplete
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from httpx import AsyncClient as AsyncClient
from pysenz import AbstractSENZAuth
from typing import override

class SENZConfigEntryAuth(AbstractSENZAuth):
    _oauth_session: Incomplete
    def __init__(self, httpx_async_client: AsyncClient, oauth_session: config_entry_oauth2_flow.OAuth2Session) -> None: ...
    @override
    async def get_access_token(self) -> str: ...
