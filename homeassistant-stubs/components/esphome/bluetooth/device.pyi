import asyncio
from _typeshed import Incomplete
from homeassistant.core import callback as callback

_LOGGER: Incomplete

class ESPHomeBluetoothDevice:
    name: str
    mac_address: str
    ble_connections_free: int
    ble_connections_limit: int
    _ble_connection_free_futures: list[asyncio.Future[int]]
    loop: asyncio.AbstractEventLoop
    def async_update_ble_connection_limits(self, free: int, limit: int) -> None: ...
    async def wait_for_ble_connections_free(self) -> int: ...
    def __init__(self, name, mac_address, ble_connections_free, ble_connections_limit, _ble_connection_free_futures, loop) -> None: ...
