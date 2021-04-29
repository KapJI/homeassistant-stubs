import abc
import logging
from abc import ABC, abstractmethod
from homeassistant.components import websocket_api as websocket_api
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.storage import Store as Store
from homeassistant.util import slugify as slugify
from typing import Any, Awaitable, Callable, Iterable

STORAGE_VERSION: int
SAVE_DELAY: int
CHANGE_ADDED: str
CHANGE_UPDATED: str
CHANGE_REMOVED: str

class CollectionChangeSet:
    change_type: str
    item_id: str
    item: Any
    def __init__(self, change_type: Any, item_id: Any, item: Any) -> None: ...
ChangeListener = Callable[[str, str, dict], Awaitable[None]]
ChangeSetListener = Callable[[Iterable[CollectionChangeSet]], Awaitable[None]]

class CollectionError(HomeAssistantError): ...

class ItemNotFound(CollectionError):
    item_id: Any = ...
    def __init__(self, item_id: str) -> None: ...

class IDManager:
    collections: Any = ...
    def __init__(self) -> None: ...
    def add_collection(self, collection: dict[str, Any]) -> None: ...
    def has_id(self, item_id: str) -> bool: ...
    def generate_id(self, suggestion: str) -> str: ...

class ObservableCollection(ABC):
    logger: Any = ...
    id_manager: Any = ...
    data: Any = ...
    listeners: Any = ...
    change_set_listeners: Any = ...
    def __init__(self, logger: logging.Logger, id_manager: Union[IDManager, None]=...) -> None: ...
    def async_items(self) -> list[dict]: ...
    def async_add_listener(self, listener: ChangeListener) -> None: ...
    def async_add_change_set_listener(self, listener: ChangeSetListener) -> None: ...
    async def notify_changes(self, change_sets: Iterable[CollectionChangeSet]) -> None: ...

class YamlCollection(ObservableCollection):
    async def async_load(self, data: list[dict]) -> None: ...

class StorageCollection(ObservableCollection, metaclass=abc.ABCMeta):
    store: Any = ...
    def __init__(self, store: Store, logger: logging.Logger, id_manager: Union[IDManager, None]=...) -> None: ...
    @property
    def hass(self) -> HomeAssistant: ...
    async def _async_load_data(self) -> Union[dict, None]: ...
    async def async_load(self) -> None: ...
    @abstractmethod
    async def _process_create_data(self, data: dict) -> dict: ...
    @abstractmethod
    def _get_suggested_id(self, info: dict) -> str: ...
    @abstractmethod
    async def _update_data(self, data: dict, update_data: dict) -> dict: ...
    async def async_create_item(self, data: dict) -> dict: ...
    async def async_update_item(self, item_id: str, updates: dict) -> dict: ...
    async def async_delete_item(self, item_id: str) -> None: ...
    def _async_schedule_save(self) -> None: ...
    def _data_to_save(self) -> dict: ...

class IDLessCollection(ObservableCollection):
    counter: int = ...
    async def async_load(self, data: list[dict]) -> None: ...

def sync_entity_lifecycle(hass: HomeAssistant, domain: str, platform: str, entity_component: EntityComponent, collection: ObservableCollection, create_entity: Callable[[dict], Entity]) -> None: ...

class StorageCollectionWebsocket:
    storage_collection: Any = ...
    api_prefix: Any = ...
    model_name: Any = ...
    create_schema: Any = ...
    update_schema: Any = ...
    def __init__(self, storage_collection: StorageCollection, api_prefix: str, model_name: str, create_schema: dict, update_schema: dict) -> None: ...
    @property
    def item_id_key(self) -> str: ...
    def async_setup(self, hass: HomeAssistant, *, create_list: bool=..., create_create: bool=...) -> None: ...
    def ws_list_item(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
    async def ws_create_item(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
    async def ws_update_item(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
    async def ws_delete_item(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
