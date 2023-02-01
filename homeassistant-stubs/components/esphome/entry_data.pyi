import asyncio
from .dashboard import async_get_dashboard as async_get_dashboard
from _typeshed import Incomplete
from aioesphomeapi import APIClient as APIClient, APIVersion, DeviceInfo, EntityInfo as EntityInfo, EntityState as EntityState, UserService
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.storage import Store as Store
from typing import Any

SAVE_DELAY: int
_LOGGER: Incomplete
INFO_TYPE_TO_PLATFORM: dict[type[EntityInfo], Platform]

class RuntimeEntryData:
    entry_id: str
    client: APIClient
    store: Store
    state: dict[type[EntityState], dict[int, EntityState]]
    info: dict[str, dict[int, EntityInfo]]
    old_info: dict[str, dict[int, EntityInfo]]
    services: dict[int, UserService]
    available: bool
    device_info: Union[DeviceInfo, None]
    api_version: APIVersion
    cleanup_callbacks: list[Callable[[], None]]
    disconnect_callbacks: list[Callable[[], None]]
    state_subscriptions: dict[tuple[type[EntityState], int], Callable[[], None]]
    loaded_platforms: set[Platform]
    platform_load_lock: asyncio.Lock
    _storage_contents: Union[dict[str, Any], None]
    ble_connections_free: int
    ble_connections_limit: int
    _ble_connection_free_futures: list[asyncio.Future[int]]
    @property
    def name(self) -> str: ...
    @property
    def friendly_name(self) -> str: ...
    @property
    def signal_static_info_updated(self) -> str: ...
    def async_update_ble_connection_limits(self, free: int, limit: int) -> None: ...
    async def wait_for_ble_connections_free(self) -> int: ...
    def async_remove_entity(self, hass: HomeAssistant, component_key: str, key: int) -> None: ...
    async def _ensure_platforms_loaded(self, hass: HomeAssistant, entry: ConfigEntry, platforms: set[Platform]) -> None: ...
    async def async_update_static_infos(self, hass: HomeAssistant, entry: ConfigEntry, infos: list[EntityInfo]) -> None: ...
    def async_subscribe_state_update(self, state_type: type[EntityState], state_key: int, entity_callback: Callable[[], None]) -> Callable[[], None]: ...
    def async_update_state(self, state: EntityState) -> None: ...
    def async_update_device_state(self, hass: HomeAssistant) -> None: ...
    async def async_load_from_store(self) -> tuple[list[EntityInfo], list[UserService]]: ...
    async def async_save_to_store(self) -> None: ...
    def __init__(self, entry_id, client, store, state, info, old_info, services, available, device_info, api_version, cleanup_callbacks, disconnect_callbacks, state_subscriptions, loaded_platforms, platform_load_lock, _storage_contents, ble_connections_free, ble_connections_limit, _ble_connection_free_futures) -> None: ...
