from .const import API_BASE_URL as API_BASE_URL
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from electrickiwi_api import AbstractAuth
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client, config_entry_oauth2_flow as config_entry_oauth2_flow

class ConfigEntryElectricKiwiAuth(AbstractAuth):
    _oauth_session: Incomplete
    def __init__(self, websession: ClientSession, oauth_session: config_entry_oauth2_flow.OAuth2Session) -> None: ...
    async def async_get_access_token(self) -> str: ...

class ConfigFlowElectricKiwiAuth(AbstractAuth):
    _token: Incomplete
    def __init__(self, hass: HomeAssistant, token: str) -> None: ...
    async def async_get_access_token(self) -> str: ...
