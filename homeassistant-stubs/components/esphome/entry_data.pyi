import asyncio
from .bluetooth.device import ESPHomeBluetoothDevice as ESPHomeBluetoothDevice
from .dashboard import async_get_dashboard as async_get_dashboard
from _typeshed import Incomplete
from aioesphomeapi import APIClient as APIClient, APIVersion, DeviceInfo, EntityInfo as EntityInfo, EntityState as EntityState, UserService
from collections.abc import Callable as Callable, Coroutine, Iterable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.storage import Store as Store
from typing import Any, Final, TypedDict

INFO_TO_COMPONENT_TYPE: Final[Incomplete]
_SENTINEL: Incomplete
SAVE_DELAY: int
_LOGGER: Incomplete
INFO_TYPE_TO_PLATFORM: dict[type[EntityInfo], Platform]

class StoreData(TypedDict, total=False):
    device_info: dict[str, Any]
    services: list[dict[str, Any]]
    api_version: dict[str, Any]

class ESPHomeStorage(Store[StoreData]): ...

class RuntimeEntryData:
    entry_id: str
    title: str
    client: APIClient
    store: ESPHomeStorage
    state: dict[type[EntityState], dict[int, EntityState]]
    stale_state: set[tuple[type[EntityState], int]]
    info: dict[type[EntityInfo], dict[int, EntityInfo]]
    services: dict[int, UserService]
    available: bool
    expected_disconnect: bool
    device_info: DeviceInfo | None
    bluetooth_device: ESPHomeBluetoothDevice | None
    api_version: APIVersion
    cleanup_callbacks: list[Callable[[], None]]
    disconnect_callbacks: list[Callable[[], None]]
    state_subscriptions: dict[tuple[type[EntityState], int], Callable[[], None]]
    loaded_platforms: set[Platform]
    platform_load_lock: asyncio.Lock
    _storage_contents: StoreData | None
    _pending_storage: Callable[[], StoreData] | None
    assist_pipeline_update_callbacks: list[Callable[[], None]]
    assist_pipeline_state: bool
    entity_info_callbacks: dict[type[EntityInfo], list[Callable[[list[EntityInfo]], None]]]
    entity_info_key_remove_callbacks: dict[tuple[type[EntityInfo], int], list[Callable[[], Coroutine[Any, Any, None]]]]
    entity_info_key_updated_callbacks: dict[tuple[type[EntityInfo], int], list[Callable[[EntityInfo], None]]]
    original_options: dict[str, Any]
    @property
    def name(self) -> str: ...
    @property
    def friendly_name(self) -> str: ...
    @property
    def signal_device_updated(self) -> str: ...
    @property
    def signal_static_info_updated(self) -> str: ...
    def async_register_static_info_callback(self, entity_info_type: type[EntityInfo], callback_: Callable[[list[EntityInfo]], None]) -> CALLBACK_TYPE: ...
    def async_register_key_static_info_remove_callback(self, static_info: EntityInfo, callback_: Callable[[], Coroutine[Any, Any, None]]) -> CALLBACK_TYPE: ...
    def async_register_key_static_info_updated_callback(self, static_info: EntityInfo, callback_: Callable[[EntityInfo], None]) -> CALLBACK_TYPE: ...
    def async_set_assist_pipeline_state(self, state: bool) -> None: ...
    def async_subscribe_assist_pipeline_update(self, update_callback: Callable[[], None]) -> Callable[[], None]: ...
    async def async_remove_entities(self, static_infos: Iterable[EntityInfo]) -> None: ...
    def async_update_entity_infos(self, static_infos: Iterable[EntityInfo]) -> None: ...
    async def _ensure_platforms_loaded(self, hass: HomeAssistant, entry: ConfigEntry, platforms: set[Platform]) -> None: ...
    async def async_update_static_infos(self, hass: HomeAssistant, entry: ConfigEntry, infos: list[EntityInfo]) -> None: ...
    def async_subscribe_state_update(self, state_type: type[EntityState], state_key: int, entity_callback: Callable[[], None]) -> Callable[[], None]: ...
    def async_update_state(self, state: EntityState) -> None: ...
    def async_update_device_state(self, hass: HomeAssistant) -> None: ...
    async def async_load_from_store(self) -> tuple[list[EntityInfo], list[UserService]]: ...
    async def async_save_to_store(self) -> None: ...
    async def async_cleanup(self) -> None: ...
    async def async_update_listener(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    def __init__(self, entry_id, title, client, store, state, stale_state, info, services, available, expected_disconnect, device_info, bluetooth_device, api_version, cleanup_callbacks, disconnect_callbacks, state_subscriptions, loaded_platforms, platform_load_lock, _storage_contents, _pending_storage, assist_pipeline_update_callbacks, assist_pipeline_state, entity_info_callbacks, entity_info_key_remove_callbacks, entity_info_key_updated_callbacks, original_options) -> None: ...
