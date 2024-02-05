from .view import HomeAssistantView as HomeAssistantView
from _typeshed import Incomplete
from aiohttp.web import Response, StreamResponse
from collections.abc import Callable
from homeassistant.auth.models import User as User
from homeassistant.exceptions import Unauthorized as Unauthorized
from typing import ParamSpec, TypeVar, overload

_HomeAssistantViewT = TypeVar('_HomeAssistantViewT', bound=HomeAssistantView)
_ResponseT = TypeVar('_ResponseT', bound=Response | StreamResponse)
_P = ParamSpec('_P')
_FuncType: Incomplete

@overload
def require_admin(_func: None = None, *, error: Unauthorized | None = None) -> Callable[[_FuncType[_HomeAssistantViewT, _P, _ResponseT]], _FuncType[_HomeAssistantViewT, _P, _ResponseT]]: ...
@overload
def require_admin(_func: _FuncType[_HomeAssistantViewT, _P, _ResponseT]) -> _FuncType[_HomeAssistantViewT, _P, _ResponseT]: ...
