from . import BackupManager as BackupManager, Folder as Folder, IncorrectPasswordError as IncorrectPasswordError, http as backup_http
from aiohttp import web
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.http import KEY_HASS as KEY_HASS
from homeassistant.components.http.data_validator import RequestDataValidator as RequestDataValidator
from homeassistant.components.onboarding import BaseOnboardingView as BaseOnboardingView, NoAuthBaseOnboardingView as NoAuthBaseOnboardingView, OnboardingStoreData as OnboardingStoreData
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate

async def async_setup_views(hass: HomeAssistant, data: OnboardingStoreData) -> None: ...
def with_backup_manager[_ViewT: BaseOnboardingView, **_P](func: Callable[Concatenate[_ViewT, BackupManager, web.Request, _P], Coroutine[Any, Any, web.Response]]) -> Callable[Concatenate[_ViewT, web.Request, _P], Coroutine[Any, Any, web.Response]]: ...

class BackupInfoView(NoAuthBaseOnboardingView):
    url: str
    name: str
    @with_backup_manager
    async def get(self, manager: BackupManager, request: web.Request) -> web.Response: ...

class RestoreBackupView(NoAuthBaseOnboardingView):
    url: str
    name: str
    @with_backup_manager
    async def post(self, manager: BackupManager, request: web.Request, data: dict[str, Any]) -> web.Response: ...

class UploadBackupView(NoAuthBaseOnboardingView, backup_http.UploadBackupView):
    url: str
    name: str
    @with_backup_manager
    async def post(self, manager: BackupManager, request: web.Request) -> web.Response: ...
