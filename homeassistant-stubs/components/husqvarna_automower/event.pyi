from . import AutomowerConfigEntry as AutomowerConfigEntry
from .const import ERROR_KEYS as ERROR_KEYS
from .coordinator import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from .entity import AutomowerBaseEntity as AutomowerBaseEntity
from _typeshed import Incomplete
from aioautomower.model import SingleMessageData as SingleMessageData
from collections.abc import Callable as Callable
from homeassistant.components.event import EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

_LOGGER: Incomplete
PARALLEL_UPDATES: int
ATTR_SEVERITY: str
ATTR_DATE_TIME: str

async def async_setup_entry(hass: HomeAssistant, config_entry: AutomowerConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AutomowerMessageEventEntity(AutomowerBaseEntity, EventEntity):
    entity_description: EventEntityDescription
    _message_cb: Callable[[SingleMessageData], None]
    _attr_translation_key: str
    _attr_event_types = ERROR_KEYS
    _attr_unique_id: Incomplete
    websocket_alive: bool
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator, *, websocket_alive: bool | None = None) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @callback
    def _handle(self, msg: SingleMessageData) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    async def async_will_remove_from_hass(self) -> None: ...
    def _handle_websocket_update(self, is_alive: bool) -> None: ...
