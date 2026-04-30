from .const import LOGGER as LOGGER
from .hub.hub import UnifiHub as UnifiHub
from _typeshed import Incomplete
from aiounifi.interfaces.api_handlers import APIHandler as APIHandler
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

POLL_INTERVAL: Incomplete

class UnifiDataUpdateCoordinator[HandlerT: APIHandler](DataUpdateCoordinator[None]):
    _handler: Incomplete
    def __init__(self, hub: UnifiHub, handler: HandlerT) -> None: ...
    @property
    def handler(self) -> HandlerT: ...
    async def _async_update_data(self) -> None: ...
