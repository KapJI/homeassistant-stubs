from typing import Any
from zeroconf import DNSRecord as DNSRecord, Zeroconf
from zeroconf.asyncio import AsyncServiceBrowser, AsyncZeroconf

TYPE_AAAA: int

class HaZeroconf(Zeroconf):
    def close(self) -> None: ...
    ha_close: Any

class HaAsyncZeroconf(AsyncZeroconf):
    async def async_close(self) -> None: ...
    ha_async_close: Any

class HaAsyncServiceBrowser(AsyncServiceBrowser):
    ipv6: Any
    def __init__(self, ipv6: bool, *args: Any, **kwargs: Any) -> None: ...
    def update_record(self, zc: Zeroconf, now: float, record: DNSRecord) -> None: ...
