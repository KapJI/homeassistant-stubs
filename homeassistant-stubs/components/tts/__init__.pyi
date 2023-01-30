from .const import DOMAIN as DOMAIN
from .media_source import generate_media_source_id as generate_media_source_id, media_source_id_to_kwargs as media_source_id_to_kwargs
from _typeshed import Incomplete
from aiohttp import web
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.components.media_player import ATTR_MEDIA_ANNOUNCE as ATTR_MEDIA_ANNOUNCE, ATTR_MEDIA_CONTENT_ID as ATTR_MEDIA_CONTENT_ID, ATTR_MEDIA_CONTENT_TYPE as ATTR_MEDIA_CONTENT_TYPE, MediaType as MediaType, SERVICE_PLAY_MEDIA as SERVICE_PLAY_MEDIA
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DESCRIPTION as CONF_DESCRIPTION, CONF_NAME as CONF_NAME, CONF_PLATFORM as CONF_PLATFORM, PLATFORM_FORMAT as PLATFORM_FORMAT
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import config_per_platform as config_per_platform, discovery as discovery
from homeassistant.helpers.network import get_url as get_url
from homeassistant.helpers.service import async_set_service_schema as async_set_service_schema
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.setup import async_prepare_setup_platform as async_prepare_setup_platform
from homeassistant.util.network import normalize_url as normalize_url
from homeassistant.util.yaml import load_yaml as load_yaml
from typing import Any, TypedDict

_LOGGER: Incomplete
TtsAudioType: Incomplete
ATTR_CACHE: str
ATTR_LANGUAGE: str
ATTR_MESSAGE: str
ATTR_OPTIONS: str
ATTR_PLATFORM: str
BASE_URL_KEY: str
CONF_BASE_URL: str
CONF_CACHE: str
CONF_CACHE_DIR: str
CONF_LANG: str
CONF_SERVICE_NAME: str
CONF_TIME_MEMORY: str
CONF_FIELDS: str
DEFAULT_CACHE: bool
DEFAULT_CACHE_DIR: str
DEFAULT_TIME_MEMORY: int
SERVICE_CLEAR_CACHE: str
SERVICE_SAY: str
_RE_VOICE_FILE: Incomplete
KEY_PATTERN: str

def _deprecated_platform(value: str) -> str: ...
def valid_base_url(value: str) -> str: ...

PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCHEMA_SERVICE_SAY: Incomplete
SCHEMA_SERVICE_CLEAR_CACHE: Incomplete

class TTSCache(TypedDict):
    filename: str
    voice: bytes

async def async_get_media_source_audio(hass: HomeAssistant, media_source_id: str) -> tuple[str, bytes]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _hash_options(options: dict) -> str: ...

class SpeechManager:
    hass: Incomplete
    providers: Incomplete
    use_cache: Incomplete
    cache_dir: Incomplete
    time_memory: Incomplete
    base_url: Incomplete
    file_cache: Incomplete
    mem_cache: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_init_cache(self, use_cache: bool, cache_dir: str, time_memory: int, base_url: Union[str, None]) -> None: ...
    async def async_clear_cache(self) -> None: ...
    def async_register_engine(self, engine: str, provider: Provider, config: ConfigType) -> None: ...
    def process_options(self, engine: str, language: Union[str, None] = ..., options: Union[dict, None] = ...) -> tuple[str, Union[dict, None]]: ...
    async def async_get_url_path(self, engine: str, message: str, cache: Union[bool, None] = ..., language: Union[str, None] = ..., options: Union[dict, None] = ...) -> str: ...
    async def async_get_tts_audio(self, engine: str, message: str, cache: Union[bool, None] = ..., language: Union[str, None] = ..., options: Union[dict, None] = ...) -> tuple[str, bytes]: ...
    def _generate_cache_key(self, message: str, language: str, options: Union[dict, None], engine: str) -> str: ...
    async def _async_get_tts_audio(self, engine: str, cache_key: str, message: str, cache: bool, language: str, options: Union[dict, None]) -> str: ...
    async def _async_save_tts_audio(self, cache_key: str, filename: str, data: bytes) -> None: ...
    async def _async_file_to_mem(self, cache_key: str) -> None: ...
    def _async_store_to_memcache(self, cache_key: str, filename: str, data: bytes) -> None: ...
    async def async_read_tts(self, filename: str) -> tuple[Union[str, None], bytes]: ...
    @staticmethod
    def write_tags(filename: str, data: bytes, provider: Provider, message: str, language: str, options: Union[dict, None]) -> bytes: ...

class Provider:
    hass: Union[HomeAssistant, None]
    name: Union[str, None]
    @property
    def default_language(self) -> Union[str, None]: ...
    @property
    def supported_languages(self) -> Union[list[str], None]: ...
    @property
    def supported_options(self) -> Union[list[str], None]: ...
    @property
    def default_options(self) -> Union[dict[str, Any], None]: ...
    def get_tts_audio(self, message: str, language: str, options: Union[dict[str, Any], None] = ...) -> TtsAudioType: ...
    async def async_get_tts_audio(self, message: str, language: str, options: Union[dict[str, Any], None] = ...) -> TtsAudioType: ...

def _init_tts_cache_dir(hass: HomeAssistant, cache_dir: str) -> str: ...
def _get_cache_files(cache_dir: str) -> dict[str, str]: ...

class TextToSpeechUrlView(HomeAssistantView):
    requires_auth: bool
    url: str
    name: str
    tts: Incomplete
    def __init__(self, tts: SpeechManager) -> None: ...
    async def post(self, request: web.Request) -> web.Response: ...

class TextToSpeechView(HomeAssistantView):
    requires_auth: bool
    url: str
    name: str
    tts: Incomplete
    def __init__(self, tts: SpeechManager) -> None: ...
    async def get(self, request: web.Request, filename: str) -> web.Response: ...

def get_base_url(hass: HomeAssistant) -> str: ...
