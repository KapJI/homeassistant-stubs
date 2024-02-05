from aiohttp import web as web
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, require_admin as require_admin
from homeassistant.components.sensor import async_update_suggested_units as async_update_suggested_units
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import check_config as check_config
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.util import location as location, unit_system as unit_system
from typing import Any

async def async_setup(hass: HomeAssistant) -> bool: ...

class CheckConfigView(HomeAssistantView):
    url: str
    name: str
    async def post(self, request: web.Request) -> web.Response: ...

async def websocket_update_config(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
async def websocket_detect_config(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
