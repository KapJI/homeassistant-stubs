import datetime as dt
from .browse_media import async_browse_media as async_browse_media
from .const import ATTR_ARTIST_NAME as ATTR_ARTIST_NAME, ATTR_CONTENT_ID as ATTR_CONTENT_ID, ATTR_FORMAT as ATTR_FORMAT, ATTR_KEYWORD as ATTR_KEYWORD, ATTR_MEDIA_TYPE as ATTR_MEDIA_TYPE, ATTR_THUMBNAIL as ATTR_THUMBNAIL, DOMAIN as DOMAIN, SERVICE_SEARCH as SERVICE_SEARCH
from .coordinator import RokuDataUpdateCoordinator as RokuDataUpdateCoordinator
from .entity import RokuEntity as RokuEntity
from .helpers import format_channel_name as format_channel_name, roku_exception_handler as roku_exception_handler
from _typeshed import Incomplete
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import ATTR_MEDIA_EXTRA as ATTR_MEDIA_EXTRA, BrowseMedia as BrowseMedia, MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType, async_process_play_media_url as async_process_play_media_url
from homeassistant.components.stream import FORMAT_CONTENT_TYPE as FORMAT_CONTENT_TYPE, HLS_PROVIDER as HLS_PROVIDER
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_NAME as ATTR_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import VolDictType as VolDictType
from typing import Any

_LOGGER: Incomplete
STREAM_FORMAT_TO_MEDIA_TYPE: Incomplete
ATTRS_TO_LAUNCH_PARAMS: Incomplete
ATTRS_TO_PLAY_ON_ROKU_PARAMS: Incomplete
ATTRS_TO_PLAY_ON_ROKU_AUDIO_PARAMS: Incomplete
SEARCH_SCHEMA: VolDictType

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RokuMediaPlayer(RokuEntity, MediaPlayerEntity):
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _attr_device_class: Incomplete
    def __init__(self, coordinator: RokuDataUpdateCoordinator) -> None: ...
    def _media_playback_trackable(self) -> bool: ...
    @property
    def state(self) -> MediaPlayerState | None: ...
    @property
    def media_content_type(self) -> MediaType | None: ...
    @property
    def media_image_url(self) -> str | None: ...
    @property
    def app_name(self) -> str | None: ...
    @property
    def app_id(self) -> str | None: ...
    @property
    def media_channel(self) -> str | None: ...
    @property
    def media_title(self) -> str | None: ...
    @property
    def media_duration(self) -> int | None: ...
    @property
    def media_position(self) -> int | None: ...
    @property
    def media_position_updated_at(self) -> dt.datetime | None: ...
    @property
    def source(self) -> str | None: ...
    @property
    def source_list(self) -> list[str]: ...
    async def search(self, keyword: str) -> None: ...
    async def async_get_browse_image(self, media_content_type: MediaType | str, media_content_id: str, media_image_id: str | None = None) -> tuple[bytes | None, str | None]: ...
    async def async_browse_media(self, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
    async def async_turn_on(self) -> None: ...
    async def async_turn_off(self) -> None: ...
    async def async_media_pause(self) -> None: ...
    async def async_media_play(self) -> None: ...
    async def async_media_play_pause(self) -> None: ...
    async def async_media_previous_track(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
    async def async_volume_up(self) -> None: ...
    async def async_volume_down(self) -> None: ...
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    async def async_select_source(self, source: str) -> None: ...
