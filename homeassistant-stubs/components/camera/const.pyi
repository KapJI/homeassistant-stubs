from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.helpers.deprecation import DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from typing import Final

DOMAIN: Final[str]
DATA_CAMERA_PREFS: Final[str]
DATA_RTSP_TO_WEB_RTC: Final[str]
PREF_PRELOAD_STREAM: Final[str]
PREF_ORIENTATION: Final[str]
SERVICE_RECORD: Final[str]
CONF_LOOKBACK: Final[str]
CONF_DURATION: Final[str]
CAMERA_STREAM_SOURCE_TIMEOUT: Final[int]
CAMERA_IMAGE_TIMEOUT: Final[int]

class StreamType(StrEnum):
    HLS: str
    WEB_RTC: str

_DEPRECATED_STREAM_TYPE_HLS: Incomplete
_DEPRECATED_STREAM_TYPE_WEB_RTC: Incomplete
__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
