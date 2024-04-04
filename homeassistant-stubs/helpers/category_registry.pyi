from .registry import BaseRegistry as BaseRegistry
from .typing import EventType as EventType, UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from _typeshed import Incomplete
from collections.abc import Iterable
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.util.ulid import ulid_now as ulid_now
from typing import Literal, TypedDict

DATA_REGISTRY: str
EVENT_CATEGORY_REGISTRY_UPDATED: str
STORAGE_KEY: str
STORAGE_VERSION_MAJOR: int

class EventCategoryRegistryUpdatedData(TypedDict):
    action: Literal['create', 'remove', 'update']
    scope: str
    category_id: str
EventCategoryRegistryUpdated = EventType[EventCategoryRegistryUpdatedData]

@dataclass(slots=True, kw_only=True, frozen=True)
class CategoryEntry:
    category_id: str = ...
    icon: str | None = ...
    name: str
    def __init__(self, *, category_id, icon, name) -> None: ...

class CategoryRegistry(BaseRegistry):
    hass: Incomplete
    categories: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_get_category(self, *, scope: str, category_id: str) -> CategoryEntry | None: ...
    def async_list_categories(self, *, scope: str) -> Iterable[CategoryEntry]: ...
    def async_create(self, *, name: str, scope: str, icon: str | None = None) -> CategoryEntry: ...
    def async_delete(self, *, scope: str, category_id: str) -> None: ...
    def async_update(self, *, scope: str, category_id: str, icon: str | None | UndefinedType = ..., name: str | UndefinedType = ...) -> CategoryEntry: ...
    async def async_load(self) -> None: ...
    def _data_to_save(self) -> dict[str, dict[str, list[dict[str, str | None]]]]: ...
    def _async_ensure_name_is_available(self, scope: str, name: str, category_id: str | None = None) -> None: ...

def async_get(hass: HomeAssistant) -> CategoryRegistry: ...
async def async_load(hass: HomeAssistant) -> None: ...