from .const import _LOGGER as _LOGGER
from .coordinator import AmazonConfigEntry as AmazonConfigEntry, AmazonDevicesCoordinator as AmazonDevicesCoordinator
from .entity import AmazonEntity as AmazonEntity
from .utils import async_remove_entity_from_virtual_group as async_remove_entity_from_virtual_group
from _typeshed import Incomplete
from homeassistant.components.event import EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final

PARALLEL_UPDATES: int
EVENTS: Final[Incomplete]
EVENT_TYPE: str

async def async_setup_entry(hass: HomeAssistant, entry: AmazonConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AlexaVoiceEvent(AmazonEntity, EventEntity):
    _attr_event_types: Incomplete
    coordinator: AmazonDevicesCoordinator
    _last_seen_timestamp: int
    @callback
    def _handle_coordinator_update(self) -> None: ...
