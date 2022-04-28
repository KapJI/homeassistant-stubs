import datetime as dt
from .browse_media import async_browse_media as async_browse_media
from .const import ATTR_ARTIST_NAME as ATTR_ARTIST_NAME, ATTR_CONTENT_ID as ATTR_CONTENT_ID, ATTR_FORMAT as ATTR_FORMAT, ATTR_KEYWORD as ATTR_KEYWORD, ATTR_MEDIA_TYPE as ATTR_MEDIA_TYPE, ATTR_THUMBNAIL as ATTR_THUMBNAIL, DOMAIN as DOMAIN, SERVICE_SEARCH as SERVICE_SEARCH
from .coordinator import RokuDataUpdateCoordinator as RokuDataUpdateCoordinator
from .entity import RokuEntity as RokuEntity
from .helpers import format_channel_name as format_channel_name, roku_exception_handler as roku_exception_handler
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import BrowseMedia as BrowseMedia, MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, async_process_play_media_url as async_process_play_media_url
from homeassistant.components.media_player.const import ATTR_MEDIA_EXTRA as ATTR_MEDIA_EXTRA, MEDIA_TYPE_APP as MEDIA_TYPE_APP, MEDIA_TYPE_CHANNEL as MEDIA_TYPE_CHANNEL, MEDIA_TYPE_MUSIC as MEDIA_TYPE_MUSIC, MEDIA_TYPE_URL as MEDIA_TYPE_URL, MEDIA_TYPE_VIDEO as MEDIA_TYPE_VIDEO
from homeassistant.components.stream.const import FORMAT_CONTENT_TYPE as FORMAT_CONTENT_TYPE, HLS_PROVIDER as HLS_PROVIDER
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_NAME as ATTR_NAME, STATE_HOME as STATE_HOME, STATE_IDLE as STATE_IDLE, STATE_ON as STATE_ON, STATE_PAUSED as STATE_PAUSED, STATE_PLAYING as STATE_PLAYING, STATE_STANDBY as STATE_STANDBY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Any
STREAM_FORMAT_TO_MEDIA_TYPE: Any
ATTRS_TO_LAUNCH_PARAMS: Any
ATTRS_TO_PLAY_ON_ROKU_PARAMS: Any
ATTRS_TO_PLAY_ON_ROKU_AUDIO_PARAMS: Any
SEARCH_SCHEMA: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RokuMediaPlayer(RokuEntity, MediaPlayerEntity):
    _attr_supported_features: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, unique_id: Union[str, None], coordinator: RokuDataUpdateCoordinator) -> None: ...
    def _media_playback_trackable(self) -> bool: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def media_content_type(self) -> Union[str, None]: ...
    @property
    def media_image_url(self) -> Union[str, None]: ...
    @property
    def app_name(self) -> Union[str, None]: ...
    @property
    def app_id(self) -> Union[str, None]: ...
    @property
    def media_channel(self) -> Union[str, None]: ...
    @property
    def media_title(self) -> Union[str, None]: ...
    @property
    def media_duration(self) -> Union[int, None]: ...
    @property
    def media_position(self) -> Union[int, None]: ...
    @property
    def media_position_updated_at(self) -> Union[dt.datetime, None]: ...
    @property
    def source(self) -> Union[str, None]: ...
    @property
    def source_list(self) -> list: ...
    async def search(self, keyword: str) -> None: ...
    async def async_get_browse_image(self, media_content_type: str, media_content_id: str, media_image_id: Union[str, None] = ...) -> tuple[Union[bytes, None], Union[str, None]]: ...
    async def async_browse_media(self, media_content_type: Union[str, None] = ..., media_content_id: Union[str, None] = ...) -> BrowseMedia: ...
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
    async def async_play_media(self, media_type: str, media_id: str, **kwargs: Any) -> None: ...
    async def async_select_source(self, source: str) -> None: ...
