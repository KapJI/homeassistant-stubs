from ..const import LOGGER as LOGGER, UNIFI_WIRELESS_CLIENTS as UNIFI_WIRELESS_CLIENTS
from ..coordinator import UnifiDataUpdateCoordinator as UnifiDataUpdateCoordinator
from ..entity import UnifiEntity as UnifiEntity, UnifiEntityDescription as UnifiEntityDescription
from .hub import UnifiHub as UnifiHub
from _typeshed import Incomplete
from aiounifi.interfaces.api_handlers import APIHandler as APIHandler
from collections.abc import Callable as Callable, Coroutine, Sequence
from homeassistant.const import Platform as Platform
from homeassistant.core import callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

CHECK_HEARTBEAT_INTERVAL: Incomplete

class UnifiEntityLoader:
    hub: Incomplete
    api_updaters: Incomplete
    wireless_clients: Incomplete
    _polling_coordinators: dict[int, UnifiDataUpdateCoordinator]
    platforms: list[tuple[AddEntitiesCallback, type[UnifiEntity], tuple[UnifiEntityDescription, ...], bool]]
    known_objects: set[tuple[str, str]]
    def __init__(self, hub: UnifiHub) -> None: ...
    async def initialize(self) -> None: ...
    async def _refresh_data(self, updaters: Sequence[Callable[[], Coroutine[Any, Any, None]]]) -> None: ...
    async def _refresh_api_data(self) -> None: ...
    @callback
    def _restore_inactive_clients(self) -> None: ...
    @callback
    def register_platform(self, async_add_entities: AddEntitiesCallback, entity_class: type[UnifiEntity], descriptions: tuple[UnifiEntityDescription, ...], requires_admin: bool = False) -> None: ...
    @callback
    def load_entities(self) -> None: ...
    @callback
    def _should_add_entity(self, description: UnifiEntityDescription, obj_id: str) -> bool: ...
    @callback
    def get_data_update_coordinator(self, handler: APIHandler) -> UnifiDataUpdateCoordinator | None: ...
    @callback
    def _load_entities(self, unifi_platform_entity: type[UnifiEntity], descriptions: tuple[UnifiEntityDescription, ...], async_add_entities: AddEntitiesCallback) -> None: ...
