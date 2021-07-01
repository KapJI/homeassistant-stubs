from homeassistant.components.media_player import ATTR_MEDIA_CONTENT_ID as ATTR_MEDIA_CONTENT_ID, ATTR_MEDIA_CONTENT_TYPE as ATTR_MEDIA_CONTENT_TYPE, ATTR_MEDIA_SEEK_POSITION as ATTR_MEDIA_SEEK_POSITION, ATTR_MEDIA_SHUFFLE as ATTR_MEDIA_SHUFFLE, ATTR_MEDIA_VOLUME_LEVEL as ATTR_MEDIA_VOLUME_LEVEL, ATTR_MEDIA_VOLUME_MUTED as ATTR_MEDIA_VOLUME_MUTED, DOMAIN as DOMAIN, MediaPlayerEntity as MediaPlayerEntity, PLATFORM_SCHEMA as PLATFORM_SCHEMA, SERVICE_CLEAR_PLAYLIST as SERVICE_CLEAR_PLAYLIST, SERVICE_MEDIA_NEXT_TRACK as SERVICE_MEDIA_NEXT_TRACK, SERVICE_MEDIA_PAUSE as SERVICE_MEDIA_PAUSE, SERVICE_MEDIA_PLAY as SERVICE_MEDIA_PLAY, SERVICE_MEDIA_PREVIOUS_TRACK as SERVICE_MEDIA_PREVIOUS_TRACK, SERVICE_MEDIA_SEEK as SERVICE_MEDIA_SEEK, SERVICE_MEDIA_STOP as SERVICE_MEDIA_STOP, SERVICE_PLAY_MEDIA as SERVICE_PLAY_MEDIA, SERVICE_SHUFFLE_SET as SERVICE_SHUFFLE_SET, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, SERVICE_VOLUME_MUTE as SERVICE_VOLUME_MUTE, SERVICE_VOLUME_SET as SERVICE_VOLUME_SET, SUPPORT_CLEAR_PLAYLIST as SUPPORT_CLEAR_PLAYLIST, SUPPORT_NEXT_TRACK as SUPPORT_NEXT_TRACK, SUPPORT_PAUSE as SUPPORT_PAUSE, SUPPORT_PLAY as SUPPORT_PLAY, SUPPORT_PLAY_MEDIA as SUPPORT_PLAY_MEDIA, SUPPORT_PREVIOUS_TRACK as SUPPORT_PREVIOUS_TRACK, SUPPORT_SEEK as SUPPORT_SEEK, SUPPORT_SHUFFLE_SET as SUPPORT_SHUFFLE_SET, SUPPORT_STOP as SUPPORT_STOP, SUPPORT_TURN_OFF as SUPPORT_TURN_OFF, SUPPORT_TURN_ON as SUPPORT_TURN_ON, SUPPORT_VOLUME_MUTE as SUPPORT_VOLUME_MUTE, SUPPORT_VOLUME_SET as SUPPORT_VOLUME_SET, SUPPORT_VOLUME_STEP as SUPPORT_VOLUME_STEP
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, EventType as EventType
from typing import Any, Callable

KEY_CLEAR_PLAYLIST: str
KEY_ON_OFF: str
KEY_PAUSE_PLAY_STOP: str
KEY_PLAY_MEDIA: str
KEY_SHUFFLE: str
KEY_SEEK: str
KEY_TRACKS: str
KEY_VOLUME: str
DEFAULT_NAME: str

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: Callable, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class MediaGroup(MediaPlayerEntity):
    _name: Any
    _state: Any
    _supported_features: int
    _entities: Any
    _features: Any
    def __init__(self, name: str, entities: list[str]) -> None: ...
    def async_on_state_change(self, event: EventType) -> None: ...
    def async_update_supported_features(self, entity_id: str, new_state: Union[State, None]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def supported_features(self) -> int: ...
    @property
    def should_poll(self) -> bool: ...
    @property
    def device_state_attributes(self) -> dict: ...
    async def async_clear_playlist(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    async def async_media_pause(self) -> None: ...
    async def async_media_play(self) -> None: ...
    async def async_media_previous_track(self) -> None: ...
    async def async_media_seek(self, position: int) -> None: ...
    async def async_media_stop(self) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
    async def async_play_media(self, media_type: str, media_id: str, **kwargs: Any) -> None: ...
    async def async_set_shuffle(self, shuffle: bool) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_turn_off(self) -> None: ...
    async def async_volume_up(self) -> None: ...
    async def async_volume_down(self) -> None: ...
    def async_update_state(self) -> None: ...
