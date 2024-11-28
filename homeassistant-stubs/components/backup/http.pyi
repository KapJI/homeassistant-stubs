from .const import DATA_MANAGER as DATA_MANAGER
from aiohttp.web import FileResponse, Request as Request, Response
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS, require_admin as require_admin
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.util import slugify as slugify

def async_register_http_views(hass: HomeAssistant) -> None: ...

class DownloadBackupView(HomeAssistantView):
    url: str
    name: str
    async def get(self, request: Request, slug: str) -> FileResponse | Response: ...

class UploadBackupView(HomeAssistantView):
    url: str
    name: str
    async def post(self, request: Request) -> Response: ...
