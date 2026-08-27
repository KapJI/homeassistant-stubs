from . import PortainerConfigEntry as PortainerConfigEntry
from .const import CONTAINER_STATE_EVENT_TYPES as CONTAINER_STATE_EVENT_TYPES
from .coordinator import PortainerContainerData as PortainerContainerData, PortainerCoordinator as PortainerCoordinator
from .entity import PortainerContainerEntity as PortainerContainerEntity, PortainerCoordinatorData as PortainerCoordinatorData
from _typeshed import Incomplete
from homeassistant.components.event import EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
CONTAINER_EVENT_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PortainerConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PortainerContainerEventEntity(PortainerContainerEntity, EventEntity):
    entity_description: EventEntityDescription
    coordinator: PortainerCoordinator
    @override
    def _handle_coordinator_update(self) -> None: ...
