from .const import DOMAIN as DOMAIN
from .coordinator import HarmanLuxuryConfigEntry as HarmanLuxuryConfigEntry, HarmanLuxuryCoordinator as HarmanLuxuryCoordinator
from _typeshed import Incomplete
from aioharmanluxury import HarmanLuxuryClient as HarmanLuxuryClient
from collections.abc import Coroutine
from datetime import datetime
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, override

PARALLEL_UPDATES: int
_VOLUME_MAX: int
_PLAY_STATE_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: HarmanLuxuryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HarmanLuxuryMediaPlayer(CoordinatorEntity[HarmanLuxuryCoordinator], MediaPlayerEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_device_class: Incomplete
    _attr_volume_step: Incomplete
    _BASE_FEATURES: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: HarmanLuxuryCoordinator) -> None: ...
    @property
    def _client(self) -> HarmanLuxuryClient: ...
    @property
    @override
    def state(self) -> MediaPlayerState: ...
    @property
    @override
    def supported_features(self) -> MediaPlayerEntityFeature: ...
    @property
    @override
    def volume_level(self) -> float: ...
    @property
    @override
    def is_volume_muted(self) -> bool: ...
    @property
    @override
    def media_title(self) -> str | None: ...
    @property
    @override
    def media_artist(self) -> str | None: ...
    @property
    @override
    def media_album_name(self) -> str | None: ...
    @property
    @override
    def media_image_url(self) -> str | None: ...
    @property
    @override
    def media_duration(self) -> int | None: ...
    @property
    @override
    def media_position(self) -> int | None: ...
    @property
    @override
    def media_position_updated_at(self) -> datetime | None: ...
    async def _async_send(self, coro: Coroutine[Any, Any, None]) -> None: ...
    @override
    async def async_set_volume_level(self, volume: float) -> None: ...
    @override
    async def async_mute_volume(self, mute: bool) -> None: ...
    @override
    async def async_media_play(self) -> None: ...
    @override
    async def async_media_pause(self) -> None: ...
    @override
    async def async_media_stop(self) -> None: ...
    @override
    async def async_media_next_track(self) -> None: ...
    @override
    async def async_media_previous_track(self) -> None: ...
