from . import KaleidescapeConfigEntry as KaleidescapeConfigEntry
from .entity import KaleidescapeEntity as KaleidescapeEntity
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.media_player import MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.dt import utcnow as utcnow
from typing import override

KALEIDESCAPE_PLAYING_STATES: Incomplete
KALEIDESCAPE_PAUSED_STATES: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: KaleidescapeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class KaleidescapeMediaPlayer(KaleidescapeEntity, MediaPlayerEntity):
    _attr_supported_features: Incomplete
    _attr_name: Incomplete
    @override
    async def async_turn_on(self) -> None: ...
    @override
    async def async_turn_off(self) -> None: ...
    @override
    async def async_media_pause(self) -> None: ...
    @override
    async def async_media_play(self) -> None: ...
    @override
    async def async_media_stop(self) -> None: ...
    @override
    async def async_media_next_track(self) -> None: ...
    @override
    async def async_media_previous_track(self) -> None: ...
    @property
    @override
    def state(self) -> MediaPlayerState: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def media_content_id(self) -> str | None: ...
    @property
    @override
    def media_content_type(self) -> str | None: ...
    @property
    @override
    def media_duration(self) -> int | None: ...
    @property
    @override
    def media_position(self) -> int | None: ...
    @property
    @override
    def media_position_updated_at(self) -> datetime | None: ...
    @property
    @override
    def media_image_url(self) -> str: ...
    @property
    @override
    def media_title(self) -> str: ...
