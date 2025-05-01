from . import http_api as cloud_http
from .const import DATA_CLOUD as DATA_CLOUD
from aiohttp import web as web
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.http import KEY_HASS as KEY_HASS
from homeassistant.components.onboarding import BaseOnboardingView as BaseOnboardingView, NoAuthBaseOnboardingView as NoAuthBaseOnboardingView, OnboardingStoreData as OnboardingStoreData
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any, Concatenate

async def async_setup_views(hass: HomeAssistant, data: OnboardingStoreData) -> None: ...
def ensure_not_done[_ViewT: BaseOnboardingView, **_P](func: Callable[Concatenate[_ViewT, web.Request, _P], Coroutine[Any, Any, web.Response]]) -> Callable[Concatenate[_ViewT, web.Request, _P], Coroutine[Any, Any, web.Response]]: ...

class CloudForgotPasswordView(NoAuthBaseOnboardingView, cloud_http.CloudForgotPasswordView):
    url: str
    name: str
    @ensure_not_done
    async def post(self, request: web.Request) -> web.Response: ...

class CloudLoginView(NoAuthBaseOnboardingView, cloud_http.CloudLoginView):
    url: str
    name: str
    @ensure_not_done
    async def post(self, request: web.Request) -> web.Response: ...

class CloudLogoutView(NoAuthBaseOnboardingView, cloud_http.CloudLogoutView):
    url: str
    name: str
    @ensure_not_done
    async def post(self, request: web.Request) -> web.Response: ...

class CloudStatusView(NoAuthBaseOnboardingView):
    url: str
    name: str
    @ensure_not_done
    async def get(self, request: web.Request) -> web.Response: ...
