from collections.abc import Callable, Coroutine
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any, Literal, overload

type _FuncType[_T] = Callable[[HomeAssistant], _T]
type _Coro[_T] = Coroutine[Any, Any, _T]
@overload
def singleton[_T](data_key: HassKey[_T], *, async_: Literal[True]) -> Callable[[_FuncType[_Coro[_T]]], _FuncType[_Coro[_T]]]: ...
@overload
def singleton[_T](data_key: HassKey[_T]) -> Callable[[_FuncType[_T]], _FuncType[_T]]: ...
@overload
def singleton[_T](data_key: str) -> Callable[[_FuncType[_T]], _FuncType[_T]]: ...
async def _test_singleton_typing(hass: HomeAssistant) -> None: ...
