from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.components.media_player import MediaPlayerState as MediaPlayerState, MediaType as MediaType, RepeatMode as RepeatMode
from mozart_api.models import Source, SourceArray
from typing import Final

class BeoSource:
    DEEZER: Final[Source]
    LINE_IN: Final[Source]
    NET_RADIO: Final[Source]
    SPDIF: Final[Source]
    TIDAL: Final[Source]
    TV: Final[Source]
    UNKNOWN: Final[Source]
    URI_STREAMER: Final[Source]

BEO_STATES: dict[str, MediaPlayerState]
BEO_REPEAT_FROM_HA: dict[RepeatMode, str]
BEO_REPEAT_TO_HA: dict[str, RepeatMode]

class BeoMediaType(StrEnum):
    DEEZER = 'deezer'
    FAVOURITE = 'favourite'
    OVERLAY_TTS = 'overlay_tts'
    RADIO = 'radio'
    TIDAL = 'tidal'
    TTS = 'provider'
    TV = 'tv'

class BeoModel(StrEnum):
    BEOCONNECT_CORE = 'Beoconnect Core'
    BEOLAB_8 = 'BeoLab 8'
    BEOLAB_28 = 'BeoLab 28'
    BEOSOUND_2 = 'Beosound 2 3rd Gen'
    BEOSOUND_A5 = 'Beosound A5'
    BEOSOUND_A9 = 'Beosound A9 5th Gen'
    BEOSOUND_BALANCE = 'Beosound Balance'
    BEOSOUND_EMERGE = 'Beosound Emerge'
    BEOSOUND_LEVEL = 'Beosound Level'
    BEOSOUND_PREMIERE = 'Beosound Premiere'
    BEOSOUND_THEATRE = 'Beosound Theatre'
    BEOREMOTE_ONE = 'Beoremote One'

class BeoAttribute(StrEnum):
    BEOLINK = 'beolink'
    BEOLINK_PEERS = 'peers'
    BEOLINK_SELF = 'self'
    BEOLINK_LEADER = 'leader'
    BEOLINK_LISTENERS = 'listeners'

class BeoButtons(StrEnum):
    BLUETOOTH = 'Bluetooth'
    MICROPHONE = 'Microphone'
    NEXT = 'Next'
    PLAY_PAUSE = 'PlayPause'
    PRESET_1 = 'Preset1'
    PRESET_2 = 'Preset2'
    PRESET_3 = 'Preset3'
    PRESET_4 = 'Preset4'
    PREVIOUS = 'Previous'
    VOLUME = 'Volume'

class WebsocketNotification(StrEnum):
    ACTIVE_LISTENING_MODE = 'active_listening_mode'
    BEO_REMOTE_BUTTON = 'beo_remote_button'
    BUTTON = 'button'
    PLAYBACK_ERROR = 'playback_error'
    PLAYBACK_METADATA = 'playback_metadata'
    PLAYBACK_PROGRESS = 'playback_progress'
    PLAYBACK_SOURCE = 'playback_source'
    PLAYBACK_STATE = 'playback_state'
    SOFTWARE_UPDATE_STATE = 'software_update_state'
    SOURCE_CHANGE = 'source_change'
    VOLUME = 'volume'
    BEOLINK = 'beolink'
    BEOLINK_PEERS = 'beolinkPeers'
    BEOLINK_LISTENERS = 'beolinkListeners'
    BEOLINK_AVAILABLE_LISTENERS = 'beolinkAvailableListeners'
    CONFIGURATION = 'configuration'
    NOTIFICATION = 'notification'
    REMOTE_CONTROL_DEVICES = 'remoteControlDevices'
    REMOTE_MENU_CHANGED = 'remoteMenuChanged'
    ALL = 'all'

DOMAIN: Final[str]
DEFAULT_MODEL: Final[str]
CONF_SERIAL_NUMBER: Final[str]
CONF_BEOLINK_JID: Final[str]
SELECTABLE_MODELS: list[str]
MANUFACTURER: Final[str]
ATTR_TYPE_NUMBER: Final[str]
ATTR_SERIAL_NUMBER: Final[str]
ATTR_ITEM_NUMBER: Final[str]
ATTR_FRIENDLY_NAME: Final[str]
BEO_ON: Final[str]
VALID_MEDIA_TYPES: Final[tuple]
FALLBACK_SOURCES: Final[SourceArray]
BEO_WEBSOCKET_EVENT: Final[str]
EVENT_TRANSLATION_MAP: dict[str, str]
CONNECTION_STATUS: Final[str]
DEVICE_BUTTONS: Final[list[str]]
DEVICE_BUTTON_EVENTS: Final[list[str]]
BEO_REMOTE_SUBMENU_CONTROL: Final[str]
BEO_REMOTE_SUBMENU_LIGHT: Final[str]
BEO_REMOTE_KEYS: Final[tuple[str, ...]]
BEO_REMOTE_CONTROL_KEYS: Final[tuple[str, ...]]
BEO_REMOTE_KEY_EVENTS: Final[list[str]]
BEOLINK_JOIN_SOURCES_TO_UPPER: Incomplete
BEOLINK_JOIN_SOURCES: Incomplete
