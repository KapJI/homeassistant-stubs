from .const import LOGGER as LOGGER
from .hub.hub import UnifiHub as UnifiHub
from _typeshed import Incomplete
from aiounifi.interfaces.api_handlers import APIHandler as APIHandler, ItemEvent
from homeassistant.core import callback as callback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

POLL_INTERVAL: Incomplete
IDLE_POLL_INTERVAL: Incomplete

class UnifiDataUpdateCoordinator[HandlerT: APIHandler](DataUpdateCoordinator[tuple[ItemEvent, str] | None]):
    _handler: Incomplete
    _disable_polling_on_endpoint_not_found: Incomplete
    _endpoint_not_found_logged: bool
    def __init__(self, hub: UnifiHub, handler: HandlerT, *, disable_polling_on_endpoint_not_found: bool = False) -> None: ...
    @property
    def handler(self) -> HandlerT: ...
    update_interval: Incomplete
    @override
    async def _async_update_data(self) -> None: ...
    @callback
    def _async_handle_update(self, event: ItemEvent, obj_id: str) -> None: ...
    @callback
    @override
    def async_update_listeners(self) -> None: ...
