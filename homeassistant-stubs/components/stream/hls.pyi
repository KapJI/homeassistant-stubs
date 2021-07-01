from . import Stream as Stream
from .const import EXT_X_START as EXT_X_START, FORMAT_CONTENT_TYPE as FORMAT_CONTENT_TYPE, HLS_PROVIDER as HLS_PROVIDER, MAX_SEGMENTS as MAX_SEGMENTS, NUM_PLAYLIST_SEGMENTS as NUM_PLAYLIST_SEGMENTS
from .core import IdleTimer as IdleTimer, PROVIDERS as PROVIDERS, StreamOutput as StreamOutput, StreamView as StreamView
from .fmp4utils import get_codec_string as get_codec_string
from aiohttp import web
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def async_setup_hls(hass: HomeAssistant) -> str: ...

class HlsMasterPlaylistView(StreamView):
    url: str
    name: str
    cors_allowed: bool
    @staticmethod
    def render(track: StreamOutput) -> str: ...
    async def handle(self, request: web.Request, stream: Stream, sequence: str) -> web.Response: ...

class HlsPlaylistView(StreamView):
    url: str
    name: str
    cors_allowed: bool
    @staticmethod
    def render(track: StreamOutput) -> str: ...
    async def handle(self, request: web.Request, stream: Stream, sequence: str) -> web.Response: ...

class HlsInitView(StreamView):
    url: str
    name: str
    cors_allowed: bool
    async def handle(self, request: web.Request, stream: Stream, sequence: str) -> web.Response: ...

class HlsSegmentView(StreamView):
    url: str
    name: str
    cors_allowed: bool
    async def handle(self, request: web.Request, stream: Stream, sequence: str) -> web.Response: ...

class HlsStreamOutput(StreamOutput):
    def __init__(self, hass: HomeAssistant, idle_timer: IdleTimer) -> None: ...
    @property
    def name(self) -> str: ...
