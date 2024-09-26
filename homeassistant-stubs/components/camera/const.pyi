from . import Camera as Camera, RtspToWebRtcProviderType as RtspToWebRtcProviderType
from .prefs import CameraPreferences as CameraPreferences
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.helpers.deprecation import DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[Camera]]
DATA_CAMERA_PREFS: HassKey[CameraPreferences]
DATA_RTSP_TO_WEB_RTC: HassKey[dict[str, RtspToWebRtcProviderType]]
PREF_PRELOAD_STREAM: Final[str]
PREF_ORIENTATION: Final[str]
SERVICE_RECORD: Final[str]
CONF_LOOKBACK: Final[str]
CONF_DURATION: Final[str]
CAMERA_STREAM_SOURCE_TIMEOUT: Final[int]
CAMERA_IMAGE_TIMEOUT: Final[int]

class CameraState(StrEnum):
    RECORDING = 'recording'
    STREAMING = 'streaming'
    IDLE = 'idle'

class StreamType(StrEnum):
    HLS = 'hls'
    WEB_RTC = 'web_rtc'

_DEPRECATED_STREAM_TYPE_HLS: Incomplete
_DEPRECATED_STREAM_TYPE_WEB_RTC: Incomplete
__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
