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

DATA_REGISTRY: HassKey[LabelRegistry]
EVENT_LABEL_REGISTRY_UPDATED: EventType[EventLabelRegistryUpdatedData]
STORAGE_KEY: str
STORAGE_VERSION_MAJOR: int

class _LabelStoreData(TypedDict):
    color: str | None
    description: str | None
    icon: str | None
    label_id: str
    name: str

class LabelRegistryStoreData(TypedDict):
    labels: list[_LabelStoreData]

class EventLabelRegistryUpdatedData(TypedDict):
    action: Literal['create', 'remove', 'update']
    label_id: str
EventLabelRegistryUpdated = Event[EventLabelRegistryUpdatedData]

@dataclass(slots=True, frozen=True, kw_only=True)
class LabelEntry(NormalizedNameBaseRegistryEntry):
    label_id: str
    description: str | None = ...
    color: str | None = ...
    icon: str | None = ...
    def __init__(self, *, name, normalized_name, label_id, description, color, icon) -> None: ...

class LabelRegistry(BaseRegistry[LabelRegistryStoreData]):
    labels: NormalizedNameBaseRegistryItems[LabelEntry]
    _label_data: dict[str, LabelEntry]
    hass: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_get_label(self, label_id: str) -> LabelEntry | None: ...
    def async_get_label_by_name(self, name: str) -> LabelEntry | None: ...
    def async_list_labels(self) -> Iterable[LabelEntry]: ...
    def _generate_id(self, name: str) -> str: ...
    def async_create(self, name: str, *, color: str | None = None, icon: str | None = None, description: str | None = None) -> LabelEntry: ...
    def async_delete(self, label_id: str) -> None: ...
    def async_update(self, label_id: str, *, color: str | None | UndefinedType = ..., description: str | None | UndefinedType = ..., icon: str | None | UndefinedType = ..., name: str | UndefinedType = ...) -> LabelEntry: ...
    async def async_load(self) -> None: ...
    def _data_to_save(self) -> LabelRegistryStoreData: ...

def async_get(hass: HomeAssistant) -> LabelRegistry: ...
async def async_load(hass: HomeAssistant) -> None: ...
