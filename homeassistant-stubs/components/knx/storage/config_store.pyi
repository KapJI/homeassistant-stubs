from ..const import DOMAIN as DOMAIN
from ..knx_entity import SIGNAL_ENTITY_REMOVE as SIGNAL_ENTITY_REMOVE
from .const import CONF_DATA as CONF_DATA
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PLATFORM as CONF_PLATFORM, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.storage import Store as Store
from homeassistant.util.ulid import ulid_now as ulid_now
from typing import Any, Final, TypedDict

_LOGGER: Incomplete
STORAGE_VERSION: Final[int]
STORAGE_KEY: Final[Incomplete]
KNXPlatformStoreModel = dict[str, dict[str, Any]]
KNXEntityStoreModel = dict[str, KNXPlatformStoreModel]

class KNXConfigStoreModel(TypedDict):
    entities: KNXEntityStoreModel

class KNXConfigStore:
    hass: Incomplete
    config_entry: Incomplete
    _store: Incomplete
    data: Incomplete
    entities: Incomplete
    async_add_entity: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
    async def load_data(self) -> None: ...
    async def create_entity(self, platform: Platform, data: dict[str, Any]) -> str | None: ...
    def get_entity_config(self, entity_id: str) -> dict[str, Any]: ...
    async def update_entity(self, platform: Platform, entity_id: str, data: dict[str, Any]) -> None: ...
    async def delete_entity(self, entity_id: str) -> None: ...
    def get_entity_entries(self) -> list[er.RegistryEntry]: ...

class ConfigStoreException(Exception): ...
