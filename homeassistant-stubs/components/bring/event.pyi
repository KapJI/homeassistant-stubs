from . import BringConfigEntry as BringConfigEntry
from .coordinator import BringDataUpdateCoordinator as BringDataUpdateCoordinator
from .entity import BringBaseEntity as BringBaseEntity
from _typeshed import Incomplete
from bring_api import BringList as BringList
from homeassistant.components.event import EventEntity as EventEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: BringConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BringEventEntity(BringBaseEntity, EventEntity):
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _attr_event_types: Incomplete
    def __init__(self, coordinator: BringDataUpdateCoordinator, bring_list: BringList) -> None: ...
    def _async_handle_event(self) -> None: ...
    @property
    def entity_picture(self) -> str | None: ...
    async def async_added_to_hass(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
