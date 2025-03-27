from . import util as util
from .agent import BackupAgent as BackupAgent
from .const import DATA_MANAGER as DATA_MANAGER
from .manager import BackupManager as BackupManager
from .models import BackupNotFound as BackupNotFound
from aiohttp.web import FileResponse, Request as Request, Response, StreamResponse
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS, require_admin as require_admin
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import frame as frame
from homeassistant.util import slugify as slugify
from multidict import istr

@callback
def async_register_http_views(hass: HomeAssistant) -> None: ...

class DownloadBackupView(HomeAssistantView):
    url: str
    name: str
    async def get(self, request: Request, backup_id: str) -> StreamResponse | FileResponse | Response: ...
    async def _send_backup_no_password(self, request: Request, headers: dict[istr, str], backup_id: str, agent_id: str, agent: BackupAgent, manager: BackupManager) -> StreamResponse | FileResponse | Response: ...
    async def _send_backup_with_password(self, hass: HomeAssistant, request: Request, headers: dict[istr, str], backup_id: str, agent_id: str, password: str, agent: BackupAgent, manager: BackupManager) -> StreamResponse | FileResponse | Response: ...

class UploadBackupView(HomeAssistantView):
    url: str
    name: str
    @require_admin
    async def post(self, request: Request) -> Response: ...
    async def _post(self, request: Request) -> Response: ...
