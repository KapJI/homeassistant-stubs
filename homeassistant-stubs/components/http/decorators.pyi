from .view import HomeAssistantView as HomeAssistantView
from _typeshed import Incomplete
from collections.abc import Callable
from homeassistant.exceptions import Unauthorized as Unauthorized
from typing import ParamSpec, TypeVar, overload

_HomeAssistantViewT = TypeVar('_HomeAssistantViewT', bound=HomeAssistantView)
_P = ParamSpec('_P')
_FuncType: Incomplete

@overload
def require_admin(_func: None = ..., *, error: Unauthorized | None = ...) -> Callable[[_FuncType[_HomeAssistantViewT, _P]], _FuncType[_HomeAssistantViewT, _P]]: ...
@overload
def require_admin(_func: _FuncType[_HomeAssistantViewT, _P]) -> _FuncType[_HomeAssistantViewT, _P]: ...
