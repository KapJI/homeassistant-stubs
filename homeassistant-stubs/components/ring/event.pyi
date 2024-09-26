from . import RingConfigEntry as RingConfigEntry
from .coordinator import RingListenCoordinator as RingListenCoordinator
from .entity import RingBaseEntity as RingBaseEntity, RingDeviceT as RingDeviceT
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from ring_doorbell import RingCapability, RingEvent as RingAlert
from typing import Generic

@dataclass(frozen=True, kw_only=True)
class RingEventEntityDescription(EventEntityDescription, Generic[RingDeviceT]):
    capability: RingCapability
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., event_types=..., capability) -> None: ...

EVENT_DESCRIPTIONS: tuple[RingEventEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: RingConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RingEvent(RingBaseEntity[RingListenCoordinator, RingDeviceT], EventEntity):
    entity_description: RingEventEntityDescription[RingDeviceT]
    _attr_unique_id: Incomplete
    def __init__(self, device: RingDeviceT, coordinator: RingListenCoordinator, description: RingEventEntityDescription[RingDeviceT]) -> None: ...
    def _async_handle_event(self, event: str) -> None: ...
    def _get_coordinator_alert(self) -> RingAlert | None: ...
    def _handle_coordinator_update(self) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_update(self) -> None: ...
