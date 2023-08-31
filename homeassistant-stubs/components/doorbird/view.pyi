from .const import API_URL as API_URL, DOMAIN as DOMAIN
from .device import async_reset_device_favorites as async_reset_device_favorites
from .util import get_door_station_by_token as get_door_station_by_token
from _typeshed import Incomplete
from aiohttp import web
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.core import HomeAssistant as HomeAssistant

class DoorBirdRequestView(HomeAssistantView):
    requires_auth: bool
    url = API_URL
    name: Incomplete
    extra_urls: Incomplete
    async def get(self, request: web.Request, event: str) -> web.Response: ...
