from .analytics import async_devices_payload as async_devices_payload
from aiohttp import web as web
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS, require_admin as require_admin
from homeassistant.core import HomeAssistant as HomeAssistant

class AnalyticsDevicesView(HomeAssistantView):
    url: str
    name: str
    @require_admin
    async def get(self, request: web.Request) -> web.Response: ...
