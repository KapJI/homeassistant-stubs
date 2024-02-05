from enum import StrEnum
from homeassistant.components.media_player import MediaPlayerState as MediaPlayerState, MediaType as MediaType
from mozart_api.models import SourceArray
from typing import Final

class SOURCE_ENUM(StrEnum):
    uriStreamer: str
    bluetooth: str
    airPlay: str
    chromeCast: str
    spotify: str
    generator: str
    lineIn: str
    spdif: str
    netRadio: str
    local: str
    dlna: str
    qplay: str
    wpl: str
    pl: str
    tv: str
    deezer: str
    beolink: str
    tidalConnect: str

BANG_OLUFSEN_STATES: dict[str, MediaPlayerState]

class BANG_OLUFSEN_MEDIA_TYPE(StrEnum):
    FAVOURITE: str
    DEEZER: str
    RADIO: str
    TTS: str

class MODEL_ENUM(StrEnum):
    BEOLAB_8: str
    BEOLAB_28: str
    BEOSOUND_2: str
    BEOSOUND_A5: str
    BEOSOUND_A9: str
    BEOSOUND_BALANCE: str
    BEOSOUND_EMERGE: str
    BEOSOUND_LEVEL: str
    BEOSOUND_THEATRE: str

class WEBSOCKET_NOTIFICATION(StrEnum):
    PLAYBACK_ERROR: Final[str]
    PLAYBACK_METADATA: Final[str]
    PLAYBACK_PROGRESS: Final[str]
    PLAYBACK_SOURCE: Final[str]
    PLAYBACK_STATE: Final[str]
    SOFTWARE_UPDATE_STATE: Final[str]
    SOURCE_CHANGE: Final[str]
    VOLUME: Final[str]
    NOTIFICATION: Final[str]
    REMOTE_MENU_CHANGED: Final[str]
    ALL: Final[str]

DOMAIN: Final[str]
DEFAULT_MODEL: Final[str]
CONF_SERIAL_NUMBER: Final[str]
CONF_BEOLINK_JID: Final[str]
COMPATIBLE_MODELS: list[str]
ATTR_TYPE_NUMBER: Final[str]
ATTR_SERIAL_NUMBER: Final[str]
ATTR_ITEM_NUMBER: Final[str]
ATTR_FRIENDLY_NAME: Final[str]
BANG_OLUFSEN_ON: Final[str]
VALID_MEDIA_TYPES: Final[tuple]
HIDDEN_SOURCE_IDS: Final[tuple]
FALLBACK_SOURCES: Final[SourceArray]
BANG_OLUFSEN_WEBSOCKET_EVENT: Final[str]
CONNECTION_STATUS: Final[str]
