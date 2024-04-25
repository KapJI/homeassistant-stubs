from _typeshed import Incomplete
from aiohttp.abc import AbstractResolver
from typing import Any, TypedDict

_NUMERIC_SOCKET_FLAGS: Incomplete
_SUPPORTS_SCOPE_ID: Incomplete

class ResolveResult(TypedDict):
    hostname: str
    host: str
    port: int
    family: int
    proto: int
    flags: int

class AsyncResolver(AbstractResolver):
    _loop: Incomplete
    _resolver: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    async def resolve(self, host: str, port: int = 0, family: int = ...) -> list[ResolveResult]: ...
    async def close(self) -> None: ...
