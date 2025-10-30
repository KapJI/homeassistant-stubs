from _typeshed import Incomplete
from enum import IntFlag, StrEnum
from homeassistant.helpers.deprecation import EnumWithDeprecatedMembers as EnumWithDeprecatedMembers

CONTENT_AUTH_EXPIRY_TIME: Incomplete
ATTR_APP_ID: str
ATTR_APP_NAME: str
ATTR_ENTITY_PICTURE_LOCAL: str
ATTR_GROUP_MEMBERS: str
ATTR_INPUT_SOURCE: str
ATTR_INPUT_SOURCE_LIST: str
ATTR_MEDIA_ANNOUNCE: str
ATTR_MEDIA_ALBUM_ARTIST: str
ATTR_MEDIA_ALBUM_NAME: str
ATTR_MEDIA_ARTIST: str
ATTR_MEDIA_CHANNEL: str
ATTR_MEDIA_CONTENT_ID: str
ATTR_MEDIA_CONTENT_TYPE: str
ATTR_MEDIA_SEARCH_QUERY: str
ATTR_MEDIA_FILTER_CLASSES: str
ATTR_MEDIA_DURATION: str
ATTR_MEDIA_ENQUEUE: str
ATTR_MEDIA_EXTRA: str
ATTR_MEDIA_EPISODE: str
ATTR_MEDIA_PLAYLIST: str
ATTR_MEDIA_POSITION: str
ATTR_MEDIA_POSITION_UPDATED_AT: str
ATTR_MEDIA_REPEAT: str
ATTR_MEDIA_SEASON: str
ATTR_MEDIA_SEEK_POSITION: str
ATTR_MEDIA_SERIES_TITLE: str
ATTR_MEDIA_SHUFFLE: str
ATTR_MEDIA_TITLE: str
ATTR_MEDIA_TRACK: str
ATTR_MEDIA_VOLUME_LEVEL: str
ATTR_MEDIA_VOLUME_MUTED: str
ATTR_SOUND_MODE: str
ATTR_SOUND_MODE_LIST: str
DOMAIN: str
INTENT_MEDIA_PAUSE: str
INTENT_MEDIA_UNPAUSE: str
INTENT_MEDIA_NEXT: str
INTENT_MEDIA_PREVIOUS: str
INTENT_PLAYER_MUTE: str
INTENT_PLAYER_UNMUTE: str
INTENT_SET_VOLUME: str
INTENT_SET_VOLUME_RELATIVE: str
INTENT_MEDIA_SEARCH_AND_PLAY: str

class MediaPlayerState(StrEnum, deprecated={'STANDBY': ('MediaPlayerState.OFF or MediaPlayerState.IDLE', '2026.8.0')}, metaclass=EnumWithDeprecatedMembers):
    OFF = 'off'
    ON = 'on'
    IDLE = 'idle'
    PLAYING = 'playing'
    PAUSED = 'paused'
    STANDBY = 'standby'
    BUFFERING = 'buffering'

class MediaClass(StrEnum):
    ALBUM = 'album'
    APP = 'app'
    ARTIST = 'artist'
    CHANNEL = 'channel'
    COMPOSER = 'composer'
    CONTRIBUTING_ARTIST = 'contributing_artist'
    DIRECTORY = 'directory'
    EPISODE = 'episode'
    GAME = 'game'
    GENRE = 'genre'
    IMAGE = 'image'
    MOVIE = 'movie'
    MUSIC = 'music'
    PLAYLIST = 'playlist'
    PODCAST = 'podcast'
    SEASON = 'season'
    TRACK = 'track'
    TV_SHOW = 'tv_show'
    URL = 'url'
    VIDEO = 'video'

class MediaType(StrEnum):
    ALBUM = 'album'
    APP = 'app'
    APPS = 'apps'
    ARTIST = 'artist'
    CHANNEL = 'channel'
    CHANNELS = 'channels'
    COMPOSER = 'composer'
    CONTRIBUTING_ARTIST = 'contributing_artist'
    EPISODE = 'episode'
    GAME = 'game'
    GENRE = 'genre'
    IMAGE = 'image'
    MOVIE = 'movie'
    MUSIC = 'music'
    PLAYLIST = 'playlist'
    PODCAST = 'podcast'
    SEASON = 'season'
    TRACK = 'track'
    TVSHOW = 'tvshow'
    URL = 'url'
    VIDEO = 'video'

SERVICE_CLEAR_PLAYLIST: str
SERVICE_JOIN: str
SERVICE_PLAY_MEDIA: str
SERVICE_BROWSE_MEDIA: str
SERVICE_SEARCH_MEDIA: str
SERVICE_SELECT_SOUND_MODE: str
SERVICE_SELECT_SOURCE: str
SERVICE_UNJOIN: str

class RepeatMode(StrEnum):
    ALL = 'all'
    OFF = 'off'
    ONE = 'one'

REPEAT_MODES: Incomplete

class MediaPlayerEntityFeature(IntFlag):
    PAUSE = 1
    SEEK = 2
    VOLUME_SET = 4
    VOLUME_MUTE = 8
    PREVIOUS_TRACK = 16
    NEXT_TRACK = 32
    TURN_ON = 128
    TURN_OFF = 256
    PLAY_MEDIA = 512
    VOLUME_STEP = 1024
    SELECT_SOURCE = 2048
    STOP = 4096
    CLEAR_PLAYLIST = 8192
    PLAY = 16384
    SHUFFLE_SET = 32768
    SELECT_SOUND_MODE = 65536
    BROWSE_MEDIA = 131072
    REPEAT_SET = 262144
    GROUPING = 524288
    MEDIA_ANNOUNCE = 1048576
    MEDIA_ENQUEUE = 2097152
    SEARCH_MEDIA = 4194304
