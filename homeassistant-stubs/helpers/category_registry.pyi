from .registry import BaseRegistry as BaseRegistry
from .singleton import singleton as singleton
from .storage import Store as Store
from .typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from _typeshed import Incomplete
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.util.dt import utc_from_timestamp as utc_from_timestamp, utcnow as utcnow
from homeassistant.util.event_type import EventType as EventType
from homeassistant.util.hass_dict import HassKey as HassKey
from homeassistant.util.ulid import ulid_now as ulid_now
from typing import Any, Literal, TypedDict

DATA_REGISTRY: HassKey[CategoryRegistry]
EVENT_CATEGORY_REGISTRY_UPDATED: EventType[EventCategoryRegistryUpdatedData]
STORAGE_KEY: str
STORAGE_VERSION_MAJOR: int
STORAGE_VERSION_MINOR: int

class _CategoryStoreData(TypedDict):
    category_id: str
    created_at: str
    icon: str | None
    modified_at: str
    name: str

class CategoryRegistryStoreData(TypedDict):
    categories: dict[str, list[_CategoryStoreData]]

class EventCategoryRegistryUpdatedData(TypedDict):
    action: Literal['create', 'remove', 'update']
    scope: str
    category_id: str

@dataclass(slots=True, kw_only=True, frozen=True)
class CategoryEntry:
    category_id: str = ...
    created_at: datetime = ...
    icon: str | None = ...
    modified_at: datetime = ...
    name: str
    def __init__(self, *, category_id=..., created_at=..., icon=..., modified_at=..., name) -> None: ...

class CategoryRegistryStore(Store[CategoryRegistryStoreData]):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, dict[str, list[dict[str, Any]]]]) -> CategoryRegistryStoreData: ...

class CategoryRegistry(BaseRegistry[CategoryRegistryStoreData]):
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
    def _data_to_save(self) -> CategoryRegistryStoreData: ...
    def _async_ensure_name_is_available(self, scope: str, name: str, category_id: str | None = None) -> None: ...

def async_get(hass: HomeAssistant) -> CategoryRegistry: ...
async def async_load(hass: HomeAssistant) -> None: ...
