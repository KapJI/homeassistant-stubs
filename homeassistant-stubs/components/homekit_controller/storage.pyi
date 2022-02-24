from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.storage import Store as Store
from typing import Any, TypedDict

ENTITY_MAP_STORAGE_KEY: Any
ENTITY_MAP_STORAGE_VERSION: int
ENTITY_MAP_SAVE_DELAY: int

class Pairing(TypedDict):
    config_num: int
    accessories: list[Any]

class StorageLayout(TypedDict):
    pairings: dict[str, Pairing]

class EntityMapStorage:
    hass: Any
    store: Any
    storage_data: Any
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_initialize(self) -> None: ...
    def get_map(self, homekit_id: str) -> Union[Pairing, None]: ...
    def async_create_or_update_map(self, homekit_id: str, config_num: int, accessories: list[Any]) -> Pairing: ...
    def async_delete_map(self, homekit_id: str) -> None: ...
    def _async_schedule_save(self) -> None: ...
    def _data_to_save(self) -> dict[str, Any]: ...
