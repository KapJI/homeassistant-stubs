from . import DOMAIN as DOMAIN, EVENT_KEY as EVENT_KEY
from .coordinator import OverseerrConfigEntry as OverseerrConfigEntry, OverseerrCoordinator as OverseerrCoordinator
from .entity import OverseerrEntity as OverseerrEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.event import EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OverseerrEventEntityDescription(EventEntityDescription):
    nullable_fields: list[str]

EVENTS: tuple[OverseerrEventEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: OverseerrConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OverseerrEvent(OverseerrEntity, EventEntity):
    entity_description: OverseerrEventEntityDescription
    _attr_available: bool
    def __init__(self, coordinator: OverseerrCoordinator, description: OverseerrEventEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_entity_picture: Incomplete
    async def _handle_update(self, event: dict[str, Any]) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @property
    def available(self) -> bool: ...

def parse_event(event: dict[str, Any], nullable_fields: list[str]) -> dict[str, Any]: ...
