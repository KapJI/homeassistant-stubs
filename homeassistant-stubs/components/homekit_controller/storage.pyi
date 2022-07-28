from .const import DOMAIN as DOMAIN, ENTITY_MAP as ENTITY_MAP
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.storage import Store as Store
from typing import Any, TypedDict

ENTITY_MAP_STORAGE_KEY: Incomplete
ENTITY_MAP_STORAGE_VERSION: int
ENTITY_MAP_SAVE_DELAY: int

class Pairing(TypedDict):
    config_num: int
    accessories: list[Any]

class StorageLayout(TypedDict):
    pairings: dict[str, Pairing]

class EntityMapStorage:
    hass: Incomplete
    store: Incomplete
    storage_data: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_initialize(self) -> None: ...
    def get_map(self, homekit_id: str) -> Union[Pairing, None]: ...
    def async_create_or_update_map(self, homekit_id: str, config_num: int, accessories: list[Any]) -> Pairing: ...
    def async_delete_map(self, homekit_id: str) -> None: ...
    def _async_schedule_save(self) -> None: ...
    def _data_to_save(self) -> StorageLayout: ...

async def async_get_entity_storage(hass: HomeAssistant) -> EntityMapStorage: ...
