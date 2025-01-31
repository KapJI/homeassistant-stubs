from _typeshed import Incomplete
from enum import IntEnum
from typing import Final

DOMAIN: str
ATTR_ENDPOINTS: str
ATTR_SETTINGS: str
ATTR_STREAMS: str
HLS_PROVIDER: str
RECORDER_PROVIDER: str
OUTPUT_FORMATS: Incomplete
SEGMENT_CONTAINER_FORMAT: Final[str]
RECORDER_CONTAINER_FORMAT: Final[str]
AUDIO_CODECS: Incomplete
FORMAT_CONTENT_TYPE: Incomplete
OUTPUT_IDLE_TIMEOUT: int
NUM_PLAYLIST_SEGMENTS: int
MAX_SEGMENTS: int
TARGET_SEGMENT_DURATION_NON_LL_HLS: float
SEGMENT_DURATION_ADJUSTER: float
EXT_X_START_NON_LL_HLS: float
EXT_X_START_LL_HLS: int
PACKETS_TO_WAIT_FOR_AUDIO: int
MAX_TIMESTAMP_GAP: int
MAX_MISSING_DTS: int
SOURCE_TIMEOUT: int
STREAM_RESTART_INCREMENT: int
STREAM_RESTART_RESET_TIME: int
CONF_LL_HLS: str
CONF_PART_DURATION: str
CONF_SEGMENT_DURATION: str
ATTR_PREFER_TCP: str
CONF_RTSP_TRANSPORT: str
RTSP_TRANSPORTS: Incomplete
CONF_USE_WALLCLOCK_AS_TIMESTAMPS: str
CONF_EXTRA_PART_WAIT_TIME: str

class StreamClientError(IntEnum):
    BadRequest = 400
    Unauthorized = 401
    Forbidden = 403
    NotFound = 404
    Other = 4
