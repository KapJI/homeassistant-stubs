import asyncio
from .const import DEFAULT_CACHE_DIR as DEFAULT_CACHE_DIR, TtsAudioType as TtsAudioType
from .entity import TTSAudioResponse as TTSAudioResponse, TextToSpeechEntity as TextToSpeechEntity
from .legacy import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE, Provider as Provider
from .media_source import generate_media_source_id as generate_media_source_id
from .models import Voice as Voice
from _typeshed import Incomplete
from aiohttp import web
from collections.abc import AsyncGenerator, MutableMapping
from dataclasses import dataclass, field
from datetime import datetime
from homeassistant.components.http import HomeAssistantView
from homeassistant.core import CALLBACK_TYPE, Event, HomeAssistant, callback
from homeassistant.helpers.typing import ConfigType
from propcache.api import cached_property
from time import monotonic
from typing import Any, Generic, Protocol, TypeVar

__all__ = ['ATTR_AUDIO_OUTPUT', 'ATTR_PREFERRED_FORMAT', 'ATTR_PREFERRED_SAMPLE_BYTES', 'ATTR_PREFERRED_SAMPLE_CHANNELS', 'ATTR_PREFERRED_SAMPLE_RATE', 'CONF_LANG', 'DEFAULT_CACHE_DIR', 'PLATFORM_SCHEMA', 'PLATFORM_SCHEMA_BASE', 'Provider', 'ResultStream', 'SampleFormat', 'TTSAudioResponse', 'TextToSpeechEntity', 'TtsAudioType', 'Voice', 'async_default_engine', 'async_get_media_source_audio', 'generate_media_source_id']

ATTR_AUDIO_OUTPUT: str
ATTR_PREFERRED_FORMAT: str
ATTR_PREFERRED_SAMPLE_RATE: str
ATTR_PREFERRED_SAMPLE_CHANNELS: str
ATTR_PREFERRED_SAMPLE_BYTES: str
CONF_LANG: str

class TTSCache:
    _result_data: bytes | None
    _partial_data: list[bytes] | None
    _loading_error: Exception | None
    _consumers: list[asyncio.Queue[bytes | None]] | None
    cache_key: Incomplete
    extension: Incomplete
    last_used: Incomplete
    _data_gen: Incomplete
    def __init__(self, cache_key: str, extension: str, data_gen: AsyncGenerator[bytes]) -> None: ...
    async def async_load_data(self) -> bytes: ...
    async def async_stream_data(self) -> AsyncGenerator[bytes]: ...

@callback
def async_default_engine(hass: HomeAssistant) -> str | None: ...
async def async_get_media_source_audio(hass: HomeAssistant, media_source_id: str) -> tuple[str, bytes]: ...

@dataclass
class ResultStream:
    last_used: float = field(default_factory=monotonic, init=False)
    token: str
    extension: str
    content_type: str
    engine: str
    use_file_cache: bool
    language: str
    options: dict
    _manager: SpeechManager
    @cached_property
    def url(self) -> str: ...
    @cached_property
    def _result_cache(self) -> asyncio.Future[TTSCache]: ...
    @callback
    def async_set_message(self, message: str) -> None: ...
    @callback
    def async_set_message_stream(self, message_stream: AsyncGenerator[str]) -> None: ...
    async def async_stream_result(self) -> AsyncGenerator[bytes]: ...

class HasLastUsed(Protocol):
    last_used: float
T = TypeVar('T', bound=HasLastUsed)

class DictCleaning(Generic[T]):
    unsub: CALLBACK_TYPE | None
    hass: Incomplete
    maxage: Incomplete
    memcache: Incomplete
    cleanup_job: Incomplete
    def __init__(self, hass: HomeAssistant, maxage: float, memcache: MutableMapping[str, T]) -> None: ...
    @callback
    def schedule(self) -> None: ...
    @callback
    def _on_hass_stop(self, event: Event) -> None: ...
    @callback
    def _cleanup(self, _now: datetime) -> None: ...

class SpeechManager:
    hass: Incomplete
    providers: dict[str, Provider]
    use_file_cache: Incomplete
    cache_dir: Incomplete
    memory_cache_maxage: Incomplete
    file_cache: dict[str, str]
    mem_cache: dict[str, TTSCache]
    token_to_stream: dict[str, ResultStream]
    memcache_cleanup: Incomplete
    token_to_stream_cleanup: Incomplete
    def __init__(self, hass: HomeAssistant, use_file_cache: bool, cache_dir: str, memory_cache_maxage: int) -> None: ...
    def _init_cache(self) -> dict[str, str]: ...
    async def async_init_cache(self) -> None: ...
    async def async_clear_cache(self) -> None: ...
    @callback
    def async_register_legacy_engine(self, engine: str, provider: Provider, config: ConfigType) -> None: ...
    @callback
    def process_options(self, engine_instance: TextToSpeechEntity | Provider, language: str | None, options: dict | None) -> tuple[str, dict[str, Any]]: ...
    @callback
    def async_get_result_stream(self, token: str) -> ResultStream | None: ...
    @callback
    def async_create_result_stream(self, engine: str, use_file_cache: bool | None = None, language: str | None = None, options: dict | None = None) -> ResultStream: ...
    @callback
    def async_cache_message_stream_in_memory(self, engine: str, message_stream: AsyncGenerator[str], language: str, options: dict) -> TTSCache: ...
    @callback
    def async_cache_message_in_memory(self, engine: str, message: str, use_file_cache: bool, language: str, options: dict) -> TTSCache: ...
    async def _load_data_into_cache(self, cache: TTSCache, engine_instance: TextToSpeechEntity | Provider, message: str, store_to_disk: bool, language: str, options: dict) -> None: ...
    async def _async_generate_tts_audio(self, engine_instance: TextToSpeechEntity | Provider, message_stream: AsyncGenerator[str], language: str, options: dict[str, Any]) -> AsyncGenerator[bytes]: ...
    async def _async_load_file(self, cache_key: str) -> AsyncGenerator[bytes]: ...
    @staticmethod
    def write_tags(filename: str, data: bytes, engine_name: str, message: str, language: str, options: dict | None) -> bytes: ...

class TextToSpeechUrlView(HomeAssistantView):
    requires_auth: bool
    url: str
    name: str
    manager: Incomplete
    def __init__(self, manager: SpeechManager) -> None: ...
    async def post(self, request: web.Request) -> web.Response: ...

class TextToSpeechView(HomeAssistantView):
    requires_auth: bool
    url: str
    name: str
    manager: Incomplete
    def __init__(self, manager: SpeechManager) -> None: ...
    async def get(self, request: web.Request, token: str) -> web.StreamResponse: ...

# Names in __all__ with no definition:
#   SampleFormat
