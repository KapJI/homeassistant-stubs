from homeassistant.backports.enum import StrEnum as StrEnum
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

STREAM_TYPE_HLS: str
STREAM_TYPE_WEB_RTC: str
