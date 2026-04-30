from . import AxisConfigEntry as AxisConfigEntry
from .entity import AxisEventDescription as AxisEventDescription, AxisEventEntity as AxisEventEntity
from _typeshed import Incomplete
from axis.models.event import Event as Event
from dataclasses import dataclass
from homeassistant.components.event import DoorbellEventType as DoorbellEventType, EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

DOORBELL_CONFIG: Incomplete

@dataclass(frozen=True, kw_only=True)
class AxisEventPlatformDescription(AxisEventDescription, EventEntityDescription): ...

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: AxisConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AxisEvent(AxisEventEntity, EventEntity):
    entity_description: AxisEventPlatformDescription
    @callback
    def async_event_callback(self, event: Event) -> None: ...
