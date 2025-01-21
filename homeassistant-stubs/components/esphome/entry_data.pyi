import asyncio
from .const import DOMAIN as DOMAIN
from .dashboard import async_get_dashboard as async_get_dashboard
from _typeshed import Incomplete
from aioesphomeapi import APIClient as APIClient, APIVersion, DeviceInfo, EntityInfo as EntityInfo, EntityState as EntityState, MediaPlayerSupportedFormat as MediaPlayerSupportedFormat, UserService
from bleak_esphome.backend.device import ESPHomeBluetoothDevice as ESPHomeBluetoothDevice
from collections import defaultdict
from collections.abc import Callable as Callable, Iterable
from dataclasses import dataclass, field
from homeassistant.components.assist_satellite import AssistSatelliteConfiguration as AssistSatelliteConfiguration
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.storage import Store as Store
from typing import Any, Final, TypedDict

type ESPHomeConfigEntry = ConfigEntry[RuntimeEntryData]
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

@dataclass(slots=True)
class RuntimeEntryData:
    entry_id: str
    title: str
    client: APIClient
    store: ESPHomeStorage
    state: defaultdict[type[EntityState], dict[int, EntityState]] = field(default_factory=Incomplete)
    stale_state: set[tuple[type[EntityState], int]] = field(default_factory=set)
    info: dict[type[EntityInfo], dict[int, EntityInfo]] = field(default_factory=dict)
    services: dict[int, UserService] = field(default_factory=dict)
    available: bool = ...
    expected_disconnect: bool = ...
    device_info: DeviceInfo | None = ...
    bluetooth_device: ESPHomeBluetoothDevice | None = ...
    api_version: APIVersion = field(default_factory=APIVersion)
    cleanup_callbacks: list[CALLBACK_TYPE] = field(default_factory=list)
    disconnect_callbacks: set[CALLBACK_TYPE] = field(default_factory=set)
    state_subscriptions: dict[tuple[type[EntityState], int], CALLBACK_TYPE] = field(default_factory=dict)
    device_update_subscriptions: set[CALLBACK_TYPE] = field(default_factory=set)
    static_info_update_subscriptions: set[Callable[[list[EntityInfo]], None]] = field(default_factory=set)
    loaded_platforms: set[Platform] = field(default_factory=set)
    platform_load_lock: asyncio.Lock = field(default_factory=asyncio.Lock)
    _storage_contents: StoreData | None = ...
    _pending_storage: Callable[[], StoreData] | None = ...
    assist_pipeline_update_callbacks: list[CALLBACK_TYPE] = field(default_factory=list)
    assist_pipeline_state: bool = ...
    entity_info_callbacks: dict[type[EntityInfo], list[Callable[[list[EntityInfo]], None]]] = field(default_factory=dict)
    entity_info_key_updated_callbacks: dict[tuple[type[EntityInfo], int], list[Callable[[EntityInfo], None]]] = field(default_factory=dict)
    original_options: dict[str, Any] = field(default_factory=dict)
    media_player_formats: dict[str, list[MediaPlayerSupportedFormat]] = field(default_factory=Incomplete)
    assist_satellite_config_update_callbacks: list[Callable[[AssistSatelliteConfiguration], None]] = field(default_factory=list)
    assist_satellite_set_wake_word_callbacks: list[Callable[[str], None]] = field(default_factory=list)
    @property
    def name(self) -> str: ...
    @property
    def friendly_name(self) -> str: ...
    @callback
    def async_register_static_info_callback(self, entity_info_type: type[EntityInfo], callback_: Callable[[list[EntityInfo]], None]) -> CALLBACK_TYPE: ...
    @callback
    def _async_unsubscribe_register_static_info(self, callbacks: list[Callable[[list[EntityInfo]], None]], callback_: Callable[[list[EntityInfo]], None]) -> None: ...
    @callback
    def async_register_key_static_info_updated_callback(self, static_info: EntityInfo, callback_: Callable[[EntityInfo], None]) -> CALLBACK_TYPE: ...
    @callback
    def _async_unsubscribe_static_key_info_updated(self, callbacks: list[Callable[[EntityInfo], None]], callback_: Callable[[EntityInfo], None]) -> None: ...
    @callback
    def async_set_assist_pipeline_state(self, state: bool) -> None: ...
    @callback
    def async_subscribe_assist_pipeline_update(self, update_callback: CALLBACK_TYPE) -> CALLBACK_TYPE: ...
    @callback
    def _async_unsubscribe_assist_pipeline_update(self, update_callback: CALLBACK_TYPE) -> None: ...
    @callback
    def async_remove_entities(self, hass: HomeAssistant, static_infos: Iterable[EntityInfo], mac: str) -> None: ...
    @callback
    def async_update_entity_infos(self, static_infos: Iterable[EntityInfo]) -> None: ...
    async def _ensure_platforms_loaded(self, hass: HomeAssistant, entry: ESPHomeConfigEntry, platforms: set[Platform]) -> None: ...
    async def async_update_static_infos(self, hass: HomeAssistant, entry: ESPHomeConfigEntry, infos: list[EntityInfo], mac: str) -> None: ...
    @callback
    def async_subscribe_device_updated(self, callback_: CALLBACK_TYPE) -> CALLBACK_TYPE: ...
    @callback
    def _async_unsubscribe_device_update(self, callback_: CALLBACK_TYPE) -> None: ...
    @callback
    def async_subscribe_static_info_updated(self, callback_: Callable[[list[EntityInfo]], None]) -> CALLBACK_TYPE: ...
    @callback
    def _async_unsubscribe_static_info_updated(self, callback_: Callable[[list[EntityInfo]], None]) -> None: ...
    @callback
    def async_subscribe_state_update(self, state_type: type[EntityState], state_key: int, entity_callback: CALLBACK_TYPE) -> CALLBACK_TYPE: ...
    @callback
    def _async_unsubscribe_state_update(self, subscription_key: tuple[type[EntityState], int]) -> None: ...
    @callback
    def async_update_state(self, state: EntityState) -> None: ...
    @callback
    def async_update_device_state(self) -> None: ...
    async def async_load_from_store(self) -> tuple[list[EntityInfo], list[UserService]]: ...
    def async_save_to_store(self) -> None: ...
    async def async_cleanup(self) -> None: ...
    async def async_update_listener(self, hass: HomeAssistant, entry: ESPHomeConfigEntry) -> None: ...
    @callback
    def async_on_disconnect(self) -> None: ...
    @callback
    def async_on_connect(self, device_info: DeviceInfo, api_version: APIVersion) -> None: ...
    @callback
    def async_register_assist_satellite_config_updated_callback(self, callback_: Callable[[AssistSatelliteConfiguration], None]) -> CALLBACK_TYPE: ...
    @callback
    def async_assist_satellite_config_updated(self, config: AssistSatelliteConfiguration) -> None: ...
    @callback
    def async_register_assist_satellite_set_wake_word_callback(self, callback_: Callable[[str], None]) -> CALLBACK_TYPE: ...
    @callback
    def async_assist_satellite_set_wake_word(self, wake_word_id: str) -> None: ...
