from .normalized_name_base_registry import NormalizedNameBaseRegistryEntry as NormalizedNameBaseRegistryEntry, NormalizedNameBaseRegistryItems as NormalizedNameBaseRegistryItems, normalize_name as normalize_name
from .registry import BaseRegistry as BaseRegistry
from .singleton import singleton as singleton
from .storage import Store as Store
from .typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from _typeshed import Incomplete
from collections.abc import Iterable
from dataclasses import dataclass
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.util import slugify as slugify
from homeassistant.util.event_type import EventType as EventType
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Literal, TypedDict

DATA_REGISTRY: HassKey[FloorRegistry]
EVENT_FLOOR_REGISTRY_UPDATED: EventType[EventFloorRegistryUpdatedData]
STORAGE_KEY: str
STORAGE_VERSION_MAJOR: int

class _FloorStoreData(TypedDict):
    aliases: list[str]
    floor_id: str
    icon: str | None
    level: int | None
    name: str

class FloorRegistryStoreData(TypedDict):
    floors: list[_FloorStoreData]

class EventFloorRegistryUpdatedData(TypedDict):
    action: Literal['create', 'remove', 'update']
    floor_id: str
EventFloorRegistryUpdated = Event[EventFloorRegistryUpdatedData]

@dataclass(slots=True, kw_only=True, frozen=True)
class FloorEntry(NormalizedNameBaseRegistryEntry):
    aliases: set[str]
    floor_id: str
    icon: str | None = ...
    level: int | None = ...
    def __init__(self, *, name, normalized_name, aliases, floor_id, icon, level) -> None: ...

class FloorRegistry(BaseRegistry[FloorRegistryStoreData]):
    floors: NormalizedNameBaseRegistryItems[FloorEntry]
    _floor_data: dict[str, FloorEntry]
    hass: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_get_floor(self, floor_id: str) -> FloorEntry | None: ...
    def async_get_floor_by_name(self, name: str) -> FloorEntry | None: ...
    def async_list_floors(self) -> Iterable[FloorEntry]: ...
    def _generate_id(self, name: str) -> str: ...
    def async_create(self, name: str, *, aliases: set[str] | None = None, icon: str | None = None, level: int | None = None) -> FloorEntry: ...
    def async_delete(self, floor_id: str) -> None: ...
    def async_update(self, floor_id: str, *, aliases: set[str] | UndefinedType = ..., icon: str | None | UndefinedType = ..., level: int | UndefinedType = ..., name: str | UndefinedType = ...) -> FloorEntry: ...
    async def async_load(self) -> None: ...
    def _data_to_save(self) -> FloorRegistryStoreData: ...

def async_get(hass: HomeAssistant) -> FloorRegistry: ...
async def async_load(hass: HomeAssistant) -> None: ...
