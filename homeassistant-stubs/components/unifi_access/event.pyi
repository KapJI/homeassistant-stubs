from .coordinator import DoorEvent as DoorEvent, UnifiAccessConfigEntry as UnifiAccessConfigEntry, UnifiAccessCoordinator as UnifiAccessCoordinator
from .entity import UnifiAccessEntity as UnifiAccessEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.event import DoorbellEventType as DoorbellEventType, EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from unifi_access_api import Door as Door

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class UnifiAccessEventEntityDescription(EventEntityDescription):
    category: str

DOORBELL_EVENT_DESCRIPTION: Incomplete
ACCESS_EVENT_DESCRIPTION: Incomplete
EVENT_DESCRIPTIONS: list[UnifiAccessEventEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: UnifiAccessConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class UnifiAccessEventEntity(UnifiAccessEntity, EventEntity):
    entity_description: UnifiAccessEventEntityDescription
    def __init__(self, coordinator: UnifiAccessCoordinator, door: Door, description: UnifiAccessEventEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_handle_event(self, event: DoorEvent) -> None: ...
