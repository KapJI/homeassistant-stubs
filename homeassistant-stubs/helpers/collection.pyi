import abc
import logging
from . import entity_registry as entity_registry
from .entity import Entity as Entity
from .entity_component import EntityComponent as EntityComponent
from .storage import Store as Store
from .typing import ConfigType as ConfigType
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Awaitable, Callable, Iterable
from homeassistant.components import websocket_api as websocket_api
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util import slugify as slugify
from typing import Any

STORAGE_VERSION: int
SAVE_DELAY: int
CHANGE_ADDED: str
CHANGE_UPDATED: str
CHANGE_REMOVED: str

class CollectionChangeSet:
    change_type: str
    item_id: str
    item: Any
    def __init__(self, change_type, item_id, item) -> None: ...
ChangeListener = Callable[[str, str, dict], Awaitable[None]]
ChangeSetListener = Callable[[Iterable[CollectionChangeSet]], Awaitable[None]]

class CollectionError(HomeAssistantError): ...

class ItemNotFound(CollectionError):
    item_id: Incomplete
    def __init__(self, item_id: str) -> None: ...

class IDManager:
    collections: Incomplete
    def __init__(self) -> None: ...
    def add_collection(self, collection: dict[str, Any]) -> None: ...
    def has_id(self, item_id: str) -> bool: ...
    def generate_id(self, suggestion: str) -> str: ...

class CollectionEntity(Entity, metaclass=abc.ABCMeta):
    @classmethod
    @abstractmethod
    def from_storage(cls, config: ConfigType) -> CollectionEntity: ...
    @classmethod
    @abstractmethod
    def from_yaml(cls, config: ConfigType) -> CollectionEntity: ...
    @abstractmethod
    async def async_update_config(self, config: ConfigType) -> None: ...

class ObservableCollection(ABC):
    logger: Incomplete
    id_manager: Incomplete
    data: Incomplete
    listeners: Incomplete
    change_set_listeners: Incomplete
    def __init__(self, logger: logging.Logger, id_manager: Union[IDManager, None] = ...) -> None: ...
    def async_items(self) -> list[dict]: ...
    def async_add_listener(self, listener: ChangeListener) -> None: ...
    def async_add_change_set_listener(self, listener: ChangeSetListener) -> None: ...
    async def notify_changes(self, change_sets: Iterable[CollectionChangeSet]) -> None: ...

class YamlCollection(ObservableCollection):
    @staticmethod
    def create_entity(entity_class: type[CollectionEntity], config: ConfigType) -> CollectionEntity: ...
    async def async_load(self, data: list[dict]) -> None: ...

class StorageCollection(ObservableCollection, metaclass=abc.ABCMeta):
    store: Incomplete
    def __init__(self, store: Store, logger: logging.Logger, id_manager: Union[IDManager, None] = ...) -> None: ...
    @staticmethod
    def create_entity(entity_class: type[CollectionEntity], config: ConfigType) -> CollectionEntity: ...
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

class IDLessCollection(YamlCollection):
    counter: int
    async def async_load(self, data: list[dict]) -> None: ...

def sync_entity_lifecycle(hass: HomeAssistant, domain: str, platform: str, entity_component: EntityComponent, collection: Union[StorageCollection, YamlCollection], entity_class: type[CollectionEntity]) -> None: ...

class StorageCollectionWebsocket:
    storage_collection: Incomplete
    api_prefix: Incomplete
    model_name: Incomplete
    create_schema: Incomplete
    update_schema: Incomplete
    def __init__(self, storage_collection: StorageCollection, api_prefix: str, model_name: str, create_schema: dict, update_schema: dict) -> None: ...
    @property
    def item_id_key(self) -> str: ...
    def async_setup(self, hass: HomeAssistant, *, create_list: bool = ..., create_create: bool = ...) -> None: ...
    def ws_list_item(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
    async def ws_create_item(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
    async def ws_update_item(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
    async def ws_delete_item(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
