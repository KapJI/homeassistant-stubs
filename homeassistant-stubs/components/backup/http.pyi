from .const import DOMAIN as DOMAIN
from .manager import BackupManager as BackupManager
from aiohttp.web import FileResponse, Request as Request, Response
from homeassistant.components.http.view import HomeAssistantView as HomeAssistantView
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.util import slugify as slugify

def async_register_http_views(hass: HomeAssistant) -> None: ...

class DownloadBackupView(HomeAssistantView):
    url: str
    name: str
    async def get(self, request: Request, slug: str) -> FileResponse | Response: ...
