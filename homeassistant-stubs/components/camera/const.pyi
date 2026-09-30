from . import Camera as Camera
from .prefs import CameraPreferences as CameraPreferences
from enum import IntFlag, StrEnum
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[Camera]]
DATA_CAMERA_PREFS: HassKey[CameraPreferences]
PREF_PRELOAD_STREAM: Final[str]
PREF_ORIENTATION: Final[str]
SERVICE_RECORD: Final[str]
SERVICE_ENABLE_MOTION: Final[str]
SERVICE_DISABLE_MOTION: Final[str]
SERVICE_SNAPSHOT: Final[str]
SERVICE_PLAY_STREAM: Final[str]
ATTR_FILENAME: Final[str]
ATTR_MEDIA_PLAYER: Final[str]
ATTR_FORMAT: Final[str]
CONF_LOOKBACK: Final[str]
CONF_DURATION: Final[str]
CAMERA_STREAM_SOURCE_TIMEOUT: Final[int]
CAMERA_IMAGE_TIMEOUT: Final[int]

class CameraEntityStateAttribute(StrEnum):
    ACCESS_TOKEN = 'access_token'
    MODEL_NAME = 'model_name'
    BRAND = 'brand'
    MOTION_DETECTION = 'motion_detection'

class CameraState(StrEnum):
    RECORDING = 'recording'
    STREAMING = 'streaming'
    IDLE = 'idle'

class StreamType(StrEnum):
    HLS = 'hls'
    WEB_RTC = 'web_rtc'

class CameraEntityFeature(IntFlag):
    ON_OFF = 1
    STREAM = 2
