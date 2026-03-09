from . import CambridgeAudioConfigEntry as CambridgeAudioConfigEntry
from .entity import CambridgeAudioEntity as CambridgeAudioEntity, command as command
from _typeshed import Incomplete
from aiostreammagic import StreamMagicClient as StreamMagicClient
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class CambridgeAudioNumberEntityDescription(NumberEntityDescription):
    exists_fn: Callable[[StreamMagicClient], bool] = ...
    value_fn: Callable[[StreamMagicClient], int]
    set_value_fn: Callable[[StreamMagicClient, int], Awaitable[None]]

def room_correction_intensity(client: StreamMagicClient) -> int: ...

CONTROL_ENTITIES: tuple[CambridgeAudioNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: CambridgeAudioConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class CambridgeAudioNumber(CambridgeAudioEntity, NumberEntity):
    entity_description: CambridgeAudioNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, client: StreamMagicClient, description: CambridgeAudioNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> int | None: ...
    @command
    async def async_set_native_value(self, value: float) -> None: ...
