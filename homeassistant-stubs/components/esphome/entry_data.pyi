import asyncio
from aioesphomeapi import APIClient as APIClient, APIVersion, DeviceInfo, EntityInfo as EntityInfo, EntityState as EntityState, UserService
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.storage import Store as Store
from typing import Any, Callable

SAVE_DELAY: int
INFO_TYPE_TO_PLATFORM: dict[type[EntityInfo], str]

class RuntimeEntryData:
    entry_id: str
    client: APIClient
    store: Store
    state: dict[str, dict[int, EntityState]]
    info: dict[str, dict[int, EntityInfo]]
    old_info: dict[str, dict[int, EntityInfo]]
    services: dict[int, UserService]
    available: bool
    device_info: Union[DeviceInfo, None]
    api_version: APIVersion
    cleanup_callbacks: list[Callable[[], None]]
    disconnect_callbacks: list[Callable[[], None]]
    loaded_platforms: set[str]
    platform_load_lock: asyncio.Lock
    _storage_contents: Union[dict[str, Any], None]
    def async_update_entity(self, hass: HomeAssistant, component_key: str, key: int) -> None: ...
    def async_remove_entity(self, hass: HomeAssistant, component_key: str, key: int) -> None: ...
    async def _ensure_platforms_loaded(self, hass: HomeAssistant, entry: ConfigEntry, platforms: set[str]) -> None: ...
    async def async_update_static_infos(self, hass: HomeAssistant, entry: ConfigEntry, infos: list[EntityInfo]) -> None: ...
    def async_update_state(self, hass: HomeAssistant, state: EntityState) -> None: ...
    def async_update_device_state(self, hass: HomeAssistant) -> None: ...
    async def async_load_from_store(self) -> tuple[list[EntityInfo], list[UserService]]: ...
    async def async_save_to_store(self) -> None: ...
