import ambiclimate
from .const import AUTH_CALLBACK_NAME as AUTH_CALLBACK_NAME, AUTH_CALLBACK_PATH as AUTH_CALLBACK_PATH, DOMAIN as DOMAIN, STORAGE_KEY as STORAGE_KEY, STORAGE_VERSION as STORAGE_VERSION
from _typeshed import Incomplete
from aiohttp import web as web
from homeassistant import config_entries as config_entries
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.network import get_url as get_url
from homeassistant.helpers.storage import Store as Store
from typing import Any

DATA_AMBICLIMATE_IMPL: str
_LOGGER: Incomplete

def register_flow_implementation(hass: HomeAssistant, client_id: str, client_secret: str) -> None: ...

class AmbiclimateFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    _registered_view: bool
    _oauth: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_auth(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_code(self, code: str | None = None) -> FlowResult: ...
    async def _get_token_info(self, code: str | None) -> dict[str, Any] | None: ...
    def _generate_view(self) -> None: ...
    def _generate_oauth(self) -> ambiclimate.AmbiclimateOAuth: ...
    def _cb_url(self) -> str: ...
    async def _get_authorize_url(self) -> str: ...

class AmbiclimateAuthCallbackView(HomeAssistantView):
    requires_auth: bool
    url = AUTH_CALLBACK_PATH
    name = AUTH_CALLBACK_NAME
    async def get(self, request: web.Request) -> str: ...
