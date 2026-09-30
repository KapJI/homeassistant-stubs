from .coordinator import PeblarAuthorizationDataUpdateCoordinator as PeblarAuthorizationDataUpdateCoordinator, PeblarConfigEntry as PeblarConfigEntry
from .entity import PeblarEntity as PeblarEntity
from _typeshed import Incomplete
from homeassistant.components.event import EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
ATTR_SESSION_NUMBER: str
ATTR_STARTED_AT: str
ATTR_TOKEN: str
EVENT_SESSION_AUTHORIZED: str
DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PeblarConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PeblarAuthorizationEventEntity(PeblarEntity[PeblarAuthorizationDataUpdateCoordinator], EventEntity):
    _session_number: int | None
    @override
    async def async_added_to_hass(self) -> None: ...
    @callback
    @override
    def _handle_coordinator_update(self) -> None: ...
