from .storage import Store as Store
from .typing import EventType as EventType, UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from _typeshed import Incomplete
from collections import UserDict
from collections.abc import Iterable, ValuesView
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.util import slugify as slugify
from typing import Literal, TypedDict

DATA_REGISTRY: str
EVENT_FLOOR_REGISTRY_UPDATED: str
STORAGE_KEY: str
STORAGE_VERSION_MAJOR: int
SAVE_DELAY: int

class EventFloorRegistryUpdatedData(TypedDict):
    action: Literal['create', 'remove', 'update']
    floor_id: str
EventFloorRegistryUpdated = EventType[EventFloorRegistryUpdatedData]

@dataclass(slots=True, kw_only=True, frozen=True)
class FloorEntry:
    aliases: set[str]
    floor_id: str
    icon: str | None = ...
    level: int = ...
    name: str
    normalized_name: str
    def __init__(self, *, aliases, floor_id, icon, level, name, normalized_name) -> None: ...

class FloorRegistryItems(UserDict[str, FloorEntry]):
    _normalized_names: Incomplete
    def __init__(self) -> None: ...
    def values(self) -> ValuesView[FloorEntry]: ...
    def __setitem__(self, key: str, entry: FloorEntry) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def get_floor_by_name(self, name: str) -> FloorEntry | None: ...

class FloorRegistry:
    floors: FloorRegistryItems
    _floor_data: dict[str, FloorEntry]
    hass: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_get_floor(self, floor_id: str) -> FloorEntry | None: ...
    def async_get_floor_by_name(self, name: str) -> FloorEntry | None: ...
    def async_list_floors(self) -> Iterable[FloorEntry]: ...
    def _generate_id(self, name: str) -> str: ...
    def async_create(self, name: str, *, aliases: set[str] | None = None, icon: str | None = None, level: int = 0) -> FloorEntry: ...
    def async_delete(self, floor_id: str) -> None: ...
    def async_update(self, floor_id: str, *, aliases: set[str] | UndefinedType = ..., icon: str | None | UndefinedType = ..., level: int | UndefinedType = ..., name: str | UndefinedType = ...) -> FloorEntry: ...
    async def async_load(self) -> None: ...
    def async_schedule_save(self) -> None: ...
    def _data_to_save(self) -> dict[str, list[dict[str, str | int | list[str] | None]]]: ...

def async_get(hass: HomeAssistant) -> FloorRegistry: ...
async def async_load(hass: HomeAssistant) -> None: ...
def _normalize_floor_name(floor_name: str) -> str: ...
