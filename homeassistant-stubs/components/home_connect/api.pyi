from _typeshed import Incomplete
from aiohomeconnect.client import AbstractAuth
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.httpx_client import get_async_client as get_async_client

class AsyncConfigEntryAuth(AbstractAuth):
    hass: Incomplete
    session: Incomplete
    def __init__(self, hass: HomeAssistant, oauth_session: config_entry_oauth2_flow.OAuth2Session) -> None: ...
    async def async_get_access_token(self) -> str: ...
