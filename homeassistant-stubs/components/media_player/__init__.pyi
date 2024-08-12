import asyncio
import collections
import datetime as dt
import logging
from .browse_media import BrowseMedia as BrowseMedia, async_process_play_media_url as async_process_play_media_url
from .const import ATTR_APP_ID as ATTR_APP_ID, ATTR_APP_NAME as ATTR_APP_NAME, ATTR_ENTITY_PICTURE_LOCAL as ATTR_ENTITY_PICTURE_LOCAL, ATTR_GROUP_MEMBERS as ATTR_GROUP_MEMBERS, ATTR_INPUT_SOURCE as ATTR_INPUT_SOURCE, ATTR_INPUT_SOURCE_LIST as ATTR_INPUT_SOURCE_LIST, ATTR_MEDIA_ALBUM_ARTIST as ATTR_MEDIA_ALBUM_ARTIST, ATTR_MEDIA_ALBUM_NAME as ATTR_MEDIA_ALBUM_NAME, ATTR_MEDIA_ANNOUNCE as ATTR_MEDIA_ANNOUNCE, ATTR_MEDIA_ARTIST as ATTR_MEDIA_ARTIST, ATTR_MEDIA_CHANNEL as ATTR_MEDIA_CHANNEL, ATTR_MEDIA_CONTENT_ID as ATTR_MEDIA_CONTENT_ID, ATTR_MEDIA_CONTENT_TYPE as ATTR_MEDIA_CONTENT_TYPE, ATTR_MEDIA_DURATION as ATTR_MEDIA_DURATION, ATTR_MEDIA_ENQUEUE as ATTR_MEDIA_ENQUEUE, ATTR_MEDIA_EPISODE as ATTR_MEDIA_EPISODE, ATTR_MEDIA_EXTRA as ATTR_MEDIA_EXTRA, ATTR_MEDIA_PLAYLIST as ATTR_MEDIA_PLAYLIST, ATTR_MEDIA_POSITION as ATTR_MEDIA_POSITION, ATTR_MEDIA_POSITION_UPDATED_AT as ATTR_MEDIA_POSITION_UPDATED_AT, ATTR_MEDIA_REPEAT as ATTR_MEDIA_REPEAT, ATTR_MEDIA_SEASON as ATTR_MEDIA_SEASON, ATTR_MEDIA_SEEK_POSITION as ATTR_MEDIA_SEEK_POSITION, ATTR_MEDIA_SERIES_TITLE as ATTR_MEDIA_SERIES_TITLE, ATTR_MEDIA_SHUFFLE as ATTR_MEDIA_SHUFFLE, ATTR_MEDIA_TITLE as ATTR_MEDIA_TITLE, ATTR_MEDIA_TRACK as ATTR_MEDIA_TRACK, ATTR_MEDIA_VOLUME_LEVEL as ATTR_MEDIA_VOLUME_LEVEL, ATTR_MEDIA_VOLUME_MUTED as ATTR_MEDIA_VOLUME_MUTED, ATTR_SOUND_MODE as ATTR_SOUND_MODE, ATTR_SOUND_MODE_LIST as ATTR_SOUND_MODE_LIST, CONTENT_AUTH_EXPIRY_TIME as CONTENT_AUTH_EXPIRY_TIME, DOMAIN as DOMAIN, MEDIA_CLASS_DIRECTORY as MEDIA_CLASS_DIRECTORY, MediaClass as MediaClass, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType, REPEAT_MODES as REPEAT_MODES, RepeatMode as RepeatMode, SERVICE_CLEAR_PLAYLIST as SERVICE_CLEAR_PLAYLIST, SERVICE_JOIN as SERVICE_JOIN, SERVICE_PLAY_MEDIA as SERVICE_PLAY_MEDIA, SERVICE_SELECT_SOUND_MODE as SERVICE_SELECT_SOUND_MODE, SERVICE_SELECT_SOURCE as SERVICE_SELECT_SOURCE, SERVICE_UNJOIN as SERVICE_UNJOIN, SUPPORT_BROWSE_MEDIA as SUPPORT_BROWSE_MEDIA, SUPPORT_CLEAR_PLAYLIST as SUPPORT_CLEAR_PLAYLIST, SUPPORT_GROUPING as SUPPORT_GROUPING, SUPPORT_NEXT_TRACK as SUPPORT_NEXT_TRACK, SUPPORT_PAUSE as SUPPORT_PAUSE, SUPPORT_PLAY as SUPPORT_PLAY, SUPPORT_PLAY_MEDIA as SUPPORT_PLAY_MEDIA, SUPPORT_PREVIOUS_TRACK as SUPPORT_PREVIOUS_TRACK, SUPPORT_REPEAT_SET as SUPPORT_REPEAT_SET, SUPPORT_SEEK as SUPPORT_SEEK, SUPPORT_SELECT_SOUND_MODE as SUPPORT_SELECT_SOUND_MODE, SUPPORT_SELECT_SOURCE as SUPPORT_SELECT_SOURCE, SUPPORT_SHUFFLE_SET as SUPPORT_SHUFFLE_SET, SUPPORT_STOP as SUPPORT_STOP, SUPPORT_TURN_OFF as SUPPORT_TURN_OFF, SUPPORT_TURN_ON as SUPPORT_TURN_ON, SUPPORT_VOLUME_MUTE as SUPPORT_VOLUME_MUTE, SUPPORT_VOLUME_SET as SUPPORT_VOLUME_SET, SUPPORT_VOLUME_STEP as SUPPORT_VOLUME_STEP
from .errors import BrowseError as BrowseError
from _typeshed import Incomplete
from aiohttp import web
from aiohttp.typedefs import LooseHeaders as LooseHeaders
from collections.abc import Callable as Callable
from enum import StrEnum
from functools import cached_property as cached_property
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_AUTHENTICATED as KEY_AUTHENTICATED
from homeassistant.components.websocket_api import ERR_NOT_SUPPORTED as ERR_NOT_SUPPORTED, ERR_UNKNOWN_ERROR as ERR_UNKNOWN_ERROR
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_PICTURE as ATTR_ENTITY_PICTURE, SERVICE_MEDIA_NEXT_TRACK as SERVICE_MEDIA_NEXT_TRACK, SERVICE_MEDIA_PAUSE as SERVICE_MEDIA_PAUSE, SERVICE_MEDIA_PLAY as SERVICE_MEDIA_PLAY, SERVICE_MEDIA_PLAY_PAUSE as SERVICE_MEDIA_PLAY_PAUSE, SERVICE_MEDIA_PREVIOUS_TRACK as SERVICE_MEDIA_PREVIOUS_TRACK, SERVICE_MEDIA_SEEK as SERVICE_MEDIA_SEEK, SERVICE_MEDIA_STOP as SERVICE_MEDIA_STOP, SERVICE_REPEAT_SET as SERVICE_REPEAT_SET, SERVICE_SHUFFLE_SET as SERVICE_SHUFFLE_SET, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, SERVICE_VOLUME_DOWN as SERVICE_VOLUME_DOWN, SERVICE_VOLUME_MUTE as SERVICE_VOLUME_MUTE, SERVICE_VOLUME_SET as SERVICE_VOLUME_SET, SERVICE_VOLUME_UP as SERVICE_VOLUME_UP, STATE_IDLE as STATE_IDLE, STATE_OFF as STATE_OFF, STATE_PLAYING as STATE_PLAYING, STATE_STANDBY as STATE_STANDBY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.network import get_url as get_url
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from typing import Any, Final, Required, TypedDict

_LOGGER: Incomplete
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete
CACHE_IMAGES: Final[str]
CACHE_MAXSIZE: Final[str]
CACHE_LOCK: Final[str]
CACHE_URL: Final[str]
CACHE_CONTENT: Final[str]

class MediaPlayerEnqueue(StrEnum):
    ADD = 'add'
    NEXT = 'next'
    PLAY = 'play'
    REPLACE = 'replace'

class MediaPlayerDeviceClass(StrEnum):
    TV = 'tv'
    SPEAKER = 'speaker'
    RECEIVER = 'receiver'

DEVICE_CLASSES_SCHEMA: Incomplete
DEVICE_CLASSES: Incomplete
DEVICE_CLASS_TV: Incomplete
DEVICE_CLASS_SPEAKER: Incomplete
DEVICE_CLASS_RECEIVER: Incomplete
MEDIA_PLAYER_PLAY_MEDIA_SCHEMA: Incomplete
ATTR_TO_PROPERTY: Incomplete

class _CacheImage(TypedDict, total=False):
    lock: Required[asyncio.Lock]
    content: tuple[bytes | None, str | None]

class _ImageCache(TypedDict):
    images: collections.OrderedDict[str, _CacheImage]
    maxsize: int

_ENTITY_IMAGE_CACHE: Incomplete

def is_on(hass: HomeAssistant, entity_id: str | None = None) -> bool: ...
def _rename_keys(**keys: Any) -> Callable[[dict[str, Any]], dict[str, Any]]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class MediaPlayerEntityDescription(EntityDescription, frozen_or_thawed=True):
    device_class: MediaPlayerDeviceClass | None
    volume_step: float | None
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., volume_step=...) -> None: ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

def _url_hash(url: str) -> str: ...

class MediaPlayerEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    _entity_component_unrecorded_attributes: Incomplete
    entity_description: MediaPlayerEntityDescription
    _access_token: str | None
    _attr_app_id: str | None
    _attr_app_name: str | None
    _attr_device_class: MediaPlayerDeviceClass | None
    _attr_group_members: list[str] | None
    _attr_is_volume_muted: bool | None
    _attr_media_album_artist: str | None
    _attr_media_album_name: str | None
    _attr_media_artist: str | None
    _attr_media_channel: str | None
    _attr_media_content_id: str | None
    _attr_media_content_type: MediaType | str | None
    _attr_media_duration: int | None
    _attr_media_episode: str | None
    _attr_media_image_hash: str | None
    _attr_media_image_remotely_accessible: bool
    _attr_media_image_url: str | None
    _attr_media_playlist: str | None
    _attr_media_position_updated_at: dt.datetime | None
    _attr_media_position: int | None
    _attr_media_season: str | None
    _attr_media_series_title: str | None
    _attr_media_title: str | None
    _attr_media_track: int | None
    _attr_repeat: RepeatMode | str | None
    _attr_shuffle: bool | None
    _attr_sound_mode_list: list[str] | None
    _attr_sound_mode: str | None
    _attr_source_list: list[str] | None
    _attr_source: str | None
    _attr_state: MediaPlayerState | None
    _attr_supported_features: MediaPlayerEntityFeature
    _attr_volume_level: float | None
    _attr_volume_step: float
    @cached_property
    def device_class(self) -> MediaPlayerDeviceClass | None: ...
    @cached_property
    def state(self) -> MediaPlayerState | None: ...
    @property
    def access_token(self) -> str: ...
    @cached_property
    def volume_level(self) -> float | None: ...
    @cached_property
    def volume_step(self) -> float: ...
    @cached_property
    def is_volume_muted(self) -> bool | None: ...
    @cached_property
    def media_content_id(self) -> str | None: ...
    @cached_property
    def media_content_type(self) -> MediaType | str | None: ...
    @cached_property
    def media_duration(self) -> int | None: ...
    @cached_property
    def media_position(self) -> int | None: ...
    @cached_property
    def media_position_updated_at(self) -> dt.datetime | None: ...
    @cached_property
    def media_image_url(self) -> str | None: ...
    @cached_property
    def media_image_remotely_accessible(self) -> bool: ...
    @property
    def media_image_hash(self) -> str | None: ...
    async def async_get_media_image(self) -> tuple[bytes | None, str | None]: ...
    async def async_get_browse_image(self, media_content_type: str, media_content_id: str, media_image_id: str | None = None) -> tuple[bytes | None, str | None]: ...
    @cached_property
    def media_title(self) -> str | None: ...
    @cached_property
    def media_artist(self) -> str | None: ...
    @cached_property
    def media_album_name(self) -> str | None: ...
    @cached_property
    def media_album_artist(self) -> str | None: ...
    @cached_property
    def media_track(self) -> int | None: ...
    @cached_property
    def media_series_title(self) -> str | None: ...
    @cached_property
    def media_season(self) -> str | None: ...
    @cached_property
    def media_episode(self) -> str | None: ...
    @cached_property
    def media_channel(self) -> str | None: ...
    @cached_property
    def media_playlist(self) -> str | None: ...
    @cached_property
    def app_id(self) -> str | None: ...
    @cached_property
    def app_name(self) -> str | None: ...
    @cached_property
    def source(self) -> str | None: ...
    @cached_property
    def source_list(self) -> list[str] | None: ...
    @cached_property
    def sound_mode(self) -> str | None: ...
    @cached_property
    def sound_mode_list(self) -> list[str] | None: ...
    @cached_property
    def shuffle(self) -> bool | None: ...
    @cached_property
    def repeat(self) -> RepeatMode | str | None: ...
    @cached_property
    def group_members(self) -> list[str] | None: ...
    @cached_property
    def supported_features(self) -> MediaPlayerEntityFeature: ...
    @property
    def supported_features_compat(self) -> MediaPlayerEntityFeature: ...
    def turn_on(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    def turn_off(self) -> None: ...
    async def async_turn_off(self) -> None: ...
    def mute_volume(self, mute: bool) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
    def set_volume_level(self, volume: float) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    def media_play(self) -> None: ...
    async def async_media_play(self) -> None: ...
    def media_pause(self) -> None: ...
    async def async_media_pause(self) -> None: ...
    def media_stop(self) -> None: ...
    async def async_media_stop(self) -> None: ...
    def media_previous_track(self) -> None: ...
    async def async_media_previous_track(self) -> None: ...
    def media_next_track(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    def media_seek(self, position: float) -> None: ...
    async def async_media_seek(self, position: float) -> None: ...
    def play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    def select_source(self, source: str) -> None: ...
    async def async_select_source(self, source: str) -> None: ...
    def select_sound_mode(self, sound_mode: str) -> None: ...
    async def async_select_sound_mode(self, sound_mode: str) -> None: ...
    def clear_playlist(self) -> None: ...
    async def async_clear_playlist(self) -> None: ...
    def set_shuffle(self, shuffle: bool) -> None: ...
    async def async_set_shuffle(self, shuffle: bool) -> None: ...
    def set_repeat(self, repeat: RepeatMode) -> None: ...
    async def async_set_repeat(self, repeat: RepeatMode) -> None: ...
    @property
    def support_play(self) -> bool: ...
    @property
    def support_pause(self) -> bool: ...
    @property
    def support_stop(self) -> bool: ...
    @property
    def support_seek(self) -> bool: ...
    @property
    def support_volume_set(self) -> bool: ...
    @property
    def support_volume_mute(self) -> bool: ...
    @property
    def support_previous_track(self) -> bool: ...
    @property
    def support_next_track(self) -> bool: ...
    @property
    def support_play_media(self) -> bool: ...
    @property
    def support_select_source(self) -> bool: ...
    @property
    def support_select_sound_mode(self) -> bool: ...
    @property
    def support_clear_playlist(self) -> bool: ...
    @property
    def support_shuffle_set(self) -> bool: ...
    @property
    def support_grouping(self) -> bool: ...
    async def async_toggle(self) -> None: ...
    async def async_volume_up(self) -> None: ...
    async def async_volume_down(self) -> None: ...
    async def async_media_play_pause(self) -> None: ...
    @property
    def entity_picture(self) -> str | None: ...
    @property
    def media_image_local(self) -> str | None: ...
    @property
    def capability_attributes(self) -> dict[str, Any]: ...
    @property
    def state_attributes(self) -> dict[str, Any]: ...
    async def async_browse_media(self, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
    def join_players(self, group_members: list[str]) -> None: ...
    async def async_join_players(self, group_members: list[str]) -> None: ...
    def unjoin_player(self) -> None: ...
    async def async_unjoin_player(self) -> None: ...
    async def _async_fetch_image_from_cache(self, url: str) -> tuple[bytes | None, str | None]: ...
    async def _async_fetch_image(self, url: str) -> tuple[bytes | None, str | None]: ...
    def get_browse_image_url(self, media_content_type: str, media_content_id: str, media_image_id: str | None = None) -> str: ...

class MediaPlayerImageView(HomeAssistantView):
    requires_auth: bool
    url: str
    name: str
    extra_urls: Incomplete
    component: Incomplete
    def __init__(self, component: EntityComponent[MediaPlayerEntity]) -> None: ...
    async def get(self, request: web.Request, entity_id: str, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> web.Response: ...

async def websocket_browse_media(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...

_FETCH_TIMEOUT: Incomplete

async def async_fetch_image(logger: logging.Logger, hass: HomeAssistant, url: str) -> tuple[bytes | None, str | None]: ...
