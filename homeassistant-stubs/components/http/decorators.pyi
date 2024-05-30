from .view import HomeAssistantView as HomeAssistantView
from _typeshed import Incomplete
from collections.abc import Callable
from homeassistant.auth.models import User as User
from homeassistant.exceptions import Unauthorized as Unauthorized
from typing import overload

_ResponseType: Incomplete
_FuncType: Incomplete

@overload
def require_admin(_func: None = None, *, error: Unauthorized | None = None) -> Callable[[_FuncType[_HomeAssistantViewT, _P, _ResponseT]], _FuncType[_HomeAssistantViewT, _P, _ResponseT]]: ...
@overload
def require_admin(_func: _FuncType[_HomeAssistantViewT, _P, _ResponseT]) -> _FuncType[_HomeAssistantViewT, _P, _ResponseT]: ...
