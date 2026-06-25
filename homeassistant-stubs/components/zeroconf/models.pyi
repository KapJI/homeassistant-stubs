from _typeshed import Incomplete
from typing import override
from zeroconf import Zeroconf
from zeroconf.asyncio import AsyncZeroconf

class HaZeroconf(Zeroconf):
    @override
    def close(self) -> None: ...
    ha_close: Incomplete

class HaAsyncZeroconf(AsyncZeroconf):
    @override
    async def async_close(self) -> None: ...
    ha_async_close: Incomplete
