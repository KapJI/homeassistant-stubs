from .const import API_URL as API_URL, CONF_PROJECT_ID as CONF_PROJECT_ID, CONF_SUBSCRIBER_ID as CONF_SUBSCRIBER_ID, DATA_NEST_CONFIG as DATA_NEST_CONFIG, DOMAIN as DOMAIN, OAUTH2_TOKEN as OAUTH2_TOKEN, SDM_SCOPES as SDM_SCOPES
from aiohttp import ClientSession as ClientSession
from google.oauth2.credentials import Credentials
from google_nest_sdm.auth import AbstractAuth
from google_nest_sdm.google_nest_subscriber import GoogleNestSubscriber
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client, config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import Any

_LOGGER: Any

class AsyncConfigEntryAuth(AbstractAuth):
    _oauth_session: Any
    _client_id: Any
    _client_secret: Any
    def __init__(self, websession: ClientSession, oauth_session: config_entry_oauth2_flow.OAuth2Session, client_id: str, client_secret: str) -> None: ...
    async def async_get_access_token(self) -> str: ...
    async def async_get_creds(self) -> Credentials: ...

async def new_subscriber(hass: HomeAssistant, entry: ConfigEntry) -> Union[GoogleNestSubscriber, None]: ...
async def new_subscriber_with_impl(hass: HomeAssistant, entry: ConfigEntry, subscriber_id: str, implementation: config_entry_oauth2_flow.AbstractOAuth2Implementation) -> GoogleNestSubscriber: ...
