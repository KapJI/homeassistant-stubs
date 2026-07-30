from .const import DOMAIN as DOMAIN
from .coordinator import SmConfigEntry as SmConfigEntry, SmDataUpdateCoordinator as SmDataUpdateCoordinator
from .entity import SmEntity as SmEntity
from _typeshed import Incomplete
from homeassistant.components.infrared import InfraredCommand as InfraredCommand, InfraredEmitterEntity as InfraredEmitterEntity, InfraredReceivedSignal as InfraredReceivedSignal, InfraredReceiverEntity as InfraredReceiverEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: SmConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SmInfraredEntity(SmEntity, InfraredEmitterEntity):
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SmDataUpdateCoordinator) -> None: ...
    @override
    async def async_send_command(self, command: InfraredCommand) -> None: ...

class SmInfraredReceiverEntity(SmEntity, InfraredReceiverEntity):
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SmDataUpdateCoordinator) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _handle_ir_code(self, timings: list[int]) -> None: ...
